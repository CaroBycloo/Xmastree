def main():
    dimension = 20
    height = 4
    width = 5
    drawTreeBody(dimension)
    drawTreeTrunk(dimension, height, width)

def getLineWidth(lineNumber):
    return lineNumber * 2 - 1

def getOffset(maxLength, width):
    return int((maxLength - width) / 2)

def drawTreeBody(dimension):
    startLine = 0
    endLine = 4
    while endLine <= dimension:
        offset = getOffset(getLineWidth(dimension), getLineWidth(endLine))
        drawTreeBodyPart(offset, startLine, endLine)
        startLine = endLine - 2
        endLine = startLine + 5

def drawTreeBodyPart(offset, startLine, endLine):
    spaces = endLine - 1 - startLine + offset
    numberOfSymbols = 1 + startLine * 2
    
    while spaces >= offset:
        line = (' ' * spaces) + ('+' * numberOfSymbols)
        spaces = spaces - 1
        numberOfSymbols = numberOfSymbols + 2
        print(line)

def drawTreeTrunk(dimension, height, width):
    maxLength = getLineWidth(dimension)
    spaces = getOffset(maxLength, width)
    line = (' ' * spaces) + ('+' * width)
    while height > 0:
        print(line)
        height = height - 1
    

if __name__ == "__main__":
    main()