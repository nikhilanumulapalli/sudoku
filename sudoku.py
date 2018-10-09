import numpy as np
import time

def validNumber(number, rowNumber, columnNumber):
    global sudoku
    if number in sudoku[rowNumber]:
        return 0
    if number in sudoku[:,columnNumber]:
        return 0
    for row in sudoku[rowNumber//3*3:(rowNumber+1)//3*3,columnNumber//3*3:(columnNumber+1)//3*3]:
        if number in row:
            return 0
    return 1

def solveSudoku():
    iterations = 0
    millis = time.time()
    count = 0
    while count < 81:
        i, j = count//9, count%9
        state = 1
        num = sudoku[i][j]
        while not sudokuState[i][j] and state:
            iterations+=1
            if num < 9:
                num += 1
            if (num < 10 and validNumber(num, i, j)):
                sudoku[i][j] = num
                state = 0
                count += 1
                i, j = count//9, count%9
                break
            elif num == 9 and not validNumber(num, i, j):
                sudoku[i][j] = 0
                count -= 1
                i, j = count//9, count%9
                while sudokuState [i][j]:
                    count -= 1
                    i, j = count//9, count%9
                break
        if count < 81 and sudokuState[i][j]:
            count += 1
            i, j = count//9, count%9

    print ('evaluation time in seconds:', time.time() - millis)
    print ("number of iterations :",iterations)
    print()

    for i in range(9):
        print(end="  ")
        for j in range(9):
            print (sudoku[i][j],end="|")
            if (j+1)%3 == 0:
                print (end="\b  ")
        if (i+1)%3:
            print("\n-----------------------")
        else:
            print("\n")

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


sudokuState = []
for row in sudoku:
    state = []
    for element in row:
        if element == 0:
            state.append(0)
        else:
            state.append(1)
    sudokuState.append(state)

solveSudoku()
