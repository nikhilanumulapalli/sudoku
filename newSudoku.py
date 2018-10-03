import numpy as np
import time

def validNumber(number, rowNumber, columnNumber):
    global sudoku
    if number in sudoku[rowNumber]:
        return 0
    if number in sudoku[:,columnNumber]:
        return 0
    for row in sudoku[rowNumber//3*3:(rowNumber//3+1)*3,columnNumber//3*3:(columnNumber//3+1)*3]:
        if number in row:
            return 0
    return 1

def updatePossibleNumbers():
    for count in range(81):
        i, j = count//9, count%9
        if not sudokuState[i][j]:
            possibleNumbers[count] = [num for num in possibleNumbers[count] if validNumber(num, i ,j)]


def insertNumber(count):
    rowNumber, columnNumber = count//9, count%9
    belongingBlocks = []
    cellNumber = (rowNumber//3)*3 + columnNumber//3
    firstNumber = 10+(cellNumber-1)*3 + (cellNumber//3)*18
    # for k in range(rowNumber*9, (rowNumber+1)*9):
    #     belongingBlocks.append(k)
    # for k in range(9+column, 73+column, 9):
    #     belongingBlocks.append(k)
    # for k in firstNumber + np.array([0,1,9,10]):
    #     belongingBlocks.append(k)
    for num in possibleNumbers[count]:
        flag = 1
        for k in range(0 + rowNumber*9, 9 + rowNumber*9):
            # print (rowNumber)
            # exit()
            if k != count and num in possibleNumbers[k]:
                flag = 0
                break
        if flag == 1:
            return num
        flag = 1
        for k in range(columnNumber, 72 + columnNumber, 9):
            if k != count and num in possibleNumbers[k]:
                flag = 0
                break
        if flag == 1:
            return num
    return 0


def validNumber2(number, rowNumber, columnNumber):
    global sudoku
    # print (sudoku[rowNumber][columnNumber])
    if sudoku[rowNumber][columnNumber] != 0:
        if list(sudoku[rowNumber]).count(number) > 1:
            print ("gone in row")
            print (number, sudoku[rowNumber])
            return 0
        if list(sudoku[:,columnNumber]).count(number) > 1:
            print ("gone in column")
            return 0
        for row in sudoku[rowNumber//3*3:(rowNumber//3+1)*3,columnNumber//3*3:(columnNumber//3+1)*3]:
            if list(row).count(number) > 1:
                print ("gone in block")
                return 0
    return 1

possibleNumbers = []
for count in range(81):
    possibleNumbers.append([])
mat = input("enter numbers")
sudoku = []
for i in mat.split(" "):
    row = []
    # print (list(i))
    for j in i:
        row.append(int(j))
    sudoku.append(row)

sudoku = np.array(sudoku)
print (sudoku)

count = 0
for row in sudoku:
    count += np.count_nonzero(row)
print (count)

sudokuState = []
for row in sudoku:
    state = []
    for element in row:
        if element == 0:
            state.append(0)
        else:
            state.append(1)
    sudokuState.append(state)
# print ('\n',np.array(sudokuState))

for count in range(81):
    i, j = count//9, count%9
    if not sudokuState[i][j]:
        possibleNumbers[count] = [num for num in range(1,10) if validNumber(num, i ,j)]
        if len(possibleNumbers[count]) == 1:
            sudoku[i][j] = possibleNumbers[count][0]
            sudokuState[i][j] = 1
            del possibleNumbers[count][0]


# print ('\n',np.array(sudokuState))
print()
# for row in sudoku:
#     print(row)
# # print()
# # for row in possibleNumbers:
# #     print (row)

# for count in range(81):
#     i, j = count//9, count%9
#     if not validNumber2(sudoku[i][j], i, j):
#         print("gone at",i,j)
#         break

for iter in range(3):
    for r in range (81):
        print (possibleNumbers[r])
    for count in range(81):
        i, j = count//9, count%9
        num = insertNumber(count)
        if num != 0:
            sudoku[i][j] = num
            del possibleNumbers[count][:]
            updatePossibleNumbers()

    print (sudoku)

    count = 0
    for row in sudoku:
        count += np.count_nonzero(row)
    print (count)

    state = 1
    while state:
        # updatePossibleNumbers()
        state = 0
        for count in range(81):
            # print (count)
            i, j = count//9, count%9
            if not sudokuState[i][j]:
                newValidNumbers = [num for num in possibleNumbers[count] if validNumber(num, i, j)]
                possibleNumbers[count] = newValidNumbers
                if len(possibleNumbers[count]) == 1:
                    # print ("state1")
                    sudoku[i][j] = possibleNumbers[count][0]
                    sudokuState[i][j] = 1
                    state = 1
                    # print ("here", count)
                    del possibleNumbers[count][0]
                    updatePossibleNumbers()
                    # print (possibleNumbers[count])
                    # break

    print (sudoku)
    count = 0
    for row in sudoku:
        count += np.count_nonzero(row)
    print (count)
    updatePossibleNumbers()
