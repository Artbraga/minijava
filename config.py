def show_help():
    print("Compilador da linguagem MiniJava")
    print("O primeiro parâmetro deve ser o nome do arquivo de entrada (localizado na pasta examples)")
    print("python main.py [file_name]")
    print("-debug\t: mostrar os resultados com prints")
    print("-tokens\t: mostrar os tokens após a execução do scanner")


class Config:
    help = False
    debug = False
    print_token_list = False

    def __init__(self, configs):
        for i in range(configs):
            c = configs[i]
            if c == "-debug":
                self.debug = True
            if c == "-tokens":
                self.print_token_list = True
            if c == "-help":
                show_help()
