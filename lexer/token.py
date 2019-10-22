from enum import Enum
import re


class Token:
    value = None
    token = None

    def __init__(self, v):
        self.match_token(v)
        if self.token is None:
            raise ValueError("Token " + v + " não identificado.")

    def match_token(self, token):
        resp = None
        for t in TokenTypes:
            if re.match(t.value, token):
                resp = t
                break
        self.token = resp
        self.value = token


class TokenTypes(Enum):
    # RESERVED WORDS
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    NULL = 'null'
    MAIN = 'main'
    CLASS = 'class'
    EXTENDS = 'extends'
    STATIC = 'static'
    THIS = 'this'
    PRINT = 'System.out.println'
    LENGTH = 'length'
    RETURN = 'return'
    NEW = 'new'
    VOID = 'void'
    PUBLIC = 'public'
    BOOLEAN_VALUE = '(true|false)'
    NUMBER = '^[-+]?[0-9]+$'
    IDENTIFIER = '(?![0-9])[a-zA-Z_][a-zA-Z_0-9]*'
    # DOUBLE OPERATORS
    EQUALS_COMPARATOR = '\=='
    NOT_EQUALS = '\!='
    AND = '\&&'
    # SIMPLE OPERATORS
    LPARENT = '\('
    RPARENT = '\)'
    LBRACE = '\{'
    RBRACE = '\}'
    LBRACKET = '\['
    RBRACKET = '\]'
    SEMICOLON = '\;'
    COMMA = '\,'
    LT = '\<'
    EQUALS = '\='
    PLUS = '\+'
    MINUS = '\-'
    ASTERISK = '\*'
    SLASH = '\/'
    EXCLAMATION = '\!'
    DOT = '.'
