import re
from lexer.token import Token


def remove_spaces(text):
    words = list()
    k = ""
    separators = [' ', '\n', '\t', '\r', '\f']
    simple_operators = ['(', ')', '[', ']', '{', '}', ';', ',', '=', '<', '+', '-', '*', '/', '!']
    double_operators = ['==', '!=', '&&']
    reserved_words = ["System.out.println"]
    for c in text:
        if len(k) > 0 and k[-1] in simple_operators:
            op = k[-1]
            if c in simple_operators:
                op = op + c
                if op not in double_operators:
                    words.append(k[:-1])
                    words.append(op[0])
                    words.append(op[1])
                else:
                    words.append(k[:-1])
                    words.append(op)
                k = ""
            elif k in simple_operators:
                words.append(k)
                if c not in separators:
                    k = c
                else:
                    k = ""
            else:
                words.append(k[:-1])
                words.append(op)
                if c not in separators:
                    k = c
                else:
                    k = ""
        elif c in separators:
            if len(k) > 0:
                words.append(k)
                k = ""
        else:
            k += c

    final_words = list()
    for w in words:
        if w not in reserved_words:
            x = w.split('.')
            for i in range(len(x)):
                if len(x[i]) > 0:
                    final_words.append(x[i])
                if i < len(x)-1:
                    final_words.append('.')
        else:
            final_words.append(w)
    return final_words


def remove_comments(string):
    # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", string)
    # remove all occurrence single-line comments (//COMMENT\n ) from string
    string = re.sub(re.compile("//.*?\n"), "", string)
    return string


def read(file_name, config):
    with open(file_name) as f:
        content = f.read()
        content = remove_comments(content)
        content = remove_spaces(content)
        if config.debug:
            print(*content, sep="\n")
        tokens = list(map(Token, content))
        if config.debug:
            [print(a.token.name, a.value) for a in tokens]
    return tokens
