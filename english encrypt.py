from abc import abstractproperty
import math

def createArray(rows,cols):
    wordArray = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append('')
        wordArray.append(row)
    return wordArray

rows,cols = 0,0
inputStr = input()
inputStr = inputStr.replace(" ", "")
length = len(inputStr)
lengthSqr = length ** 0.5
rows = math.floor(lengthSqr)
cols = math.ceil(lengthSqr)
if rows * cols < length:
    rows += 1
wordList = createArray(rows,cols)
count = 0
for x in range(rows):   
    for j in range(cols):
        wordList[x][j] = inputStr[count] 
        if count == len(inputStr)-1:
            break
        count += 1
for horizontal in range(cols):
    for verticle in range(rows):
        print(wordList[verticle][horizontal],end="")
    print(end=" ")
