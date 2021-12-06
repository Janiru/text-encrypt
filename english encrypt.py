from abc import abstractproperty
import math

def createArray(rows,cols):
    wordArray = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        wordArray.append(row)
    return wordArray

rows,cols = 0,0
inputStr = input()
inputStr = inputStr.replace(" ", "")
length = len(inputStr)
lengthSqr = length ** 0.5
rows = math.floor(lengthSqr)
cols = math.ceil(lengthSqr)
wordList = createArray(rows,cols)
count = 0
print(f"rows {rows} cols {cols}")
for x in range(rows):
    for j in range(cols):
        wordList[x][j] = inputStr[count]
        count += 1
for i in wordList:
    for x in i:
        print(x, end=" ")
    print()



