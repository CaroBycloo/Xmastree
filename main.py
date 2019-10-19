import colorama
from colorama import Fore, Back, Style
CLEAR_SCREEN = '\033[2J'

def main():
    colorama.init()
    print(CLEAR_SCREEN)
    dimension = 10
    height = 4
    width = 5
    drawTreeBodyPart(6, 0, 4)
    drawTreeBodyPart(3, 2, 7)
    drawTreeBodyPart(0, 5, 10)
    drawTreeTrunk(dimension, height, width)

def drawTreeBodyPart(offset, startLine, endLine):
    spaces = endLine - 1 - startLine + offset
    numberOfSymbols = 1 + startLine * 2
    while spaces >= offset:
        line = (' ' * spaces) + ('+' * numberOfSymbols)
        spaces = spaces - 1
        numberOfSymbols = numberOfSymbols + 2
        print(Fore.GREEN + line)

def drawTreeTrunk(dimension, height, width):
    maxLength = dimension * 2 - 1
    spaces = int((maxLength - width) / 2)
    line = (' ' * spaces) + ('+' * width)
    while height > 0:
        print(Fore.WHITE + line)
        height = height - 1
    

if __name__ == "__main__":
    main()