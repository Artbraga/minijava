import sys

from config import Config
from lexer.lexer import read


def main():
    config = Config(sys.argv)
    if config.help:
        return
    file_name = "./examples/" + sys.argv[1]
    tokens = read(file_name, config)

main()
