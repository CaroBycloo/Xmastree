def main():
    dimension = 10
    height = 4
    width = 5
    drawTreeBody(dimension)
    drawTreeTrunk(dimension, height, width)

def drawTreeBody(dimension):
    spaces = dimension - 1
    symbol = 1
    
    while spaces >= 0:
        line = (' ' * spaces) + ('+' * symbol)
        spaces = spaces - 1
        symbol = symbol + 2
        print(line)

def drawTreeTrunk(dimension, height, width):
    maxLength = dimension * 2 - 1
    spaces = int((maxLength - width) / 2)
    line = (' ' * spaces) + ('+' * width)
    while height > 0:
        print(line)
        height = height - 1
    

if __name__ == "__main__":
    main()