from cmu_112_graphics import *
from TilesClass import *
from UnitClass import *
from PlayerClass import *

player1 = Player("Player 1")
player2 = Player("Player 2")
player3 = Player("Player 3")
tempBoard = [[Forest(0,0), Field(0, 1), Field(0,2), Mountain(0,3), Field(0,4), Forest(0,5), Field(0,6), Field(0,7), Field(0,8), Field(0,9), Field(0,10)],
             [Field(1,0), Mountain(1,1), Mountain(1,2), Forest(1,3), Forest(1,4), Forest(1,5), Field(1,6), Field(1,7), Forest(1,8), Forest(1,9), Field(1,10)],
             [Forest(2,0), City(2,1, player3), Forest(2,2), Field(2,3), Forest(2,4), Capital(2,5, player3), Forest(2,6), Forest(2,7), Field(2,8), Forest(2,9), Field(2,10)],
             [Mountain(3,0), Forest(3,1), Mountain(3,2), Forest(3,3), Mountain(3,4), Mountain(3,5), Field(3,6), Field(3,7), Mountain(3,8), Field(3,9), Forest(3,10)],
             [Forest(4,0), Forest(4,1), Field(4,2), Forest(4,3), Mountain(4,4), Field(4,5), Forest(4,6), Field(4,7), Field(4,8), Field(4,9), Mountain(4,10)],
             [Field(5,0), Capital(5,1,player1), Field(5,2), Field(5,3), Forest(5,4), Mountain(5,5), Mountain(5,6), Forest(5,7),Field(5,8), Forest(5,9), Mountain(5, 10)],
             [Forest(6,0), Forest(6,1), Forest(6,2), Forest(6,3), Forest(6,4), Forest(6,5), Field(6,6), Forest(6,7), Forest(6,8), Field(6,9), Mountain(6,10)],
             [Mountain(7,0), Forest(7,1), Field(7,2), Field(7,3), Mountain(7,5), Forest(7,5), City(7,6,player2), Field(7,7), Field(7,8), Field(7,9), Field(7,10)],
             [Forest(8,0), Field(8,1), City(8,2,player1), Forest(8,3), Field(8,4), Field(8,5), Mountain(8,6), Field(8,7), Field(8,8), Forest(8,9), Field(8,10)],
             [Field(9,0), Field(9,1), Forest(9,2), Field(9,3), Forest(9,4), Forest(9,5), Forest(9,6), Field(9,7), Field(9,8), Capital(9,9,player2), Mountain(9,10)],
             [Field(10,0), Field(10,1), Forest(10,2), Forest(10,3), Field(10,4), Field(10,5), Field(10,6), Field(10,7), Field(10,8), Forest(10,9), Forest(10,10)]]

# def recursivePrint(L):
#     if L == []:
#         return []
#     elif isinstance(L[0], list):
#         return recursivePrint(L[0]) + recursivePrint(L[1:])
#     else:
#         print(L[0], (L[0].x, L[0].y))
#         return [L[0]] + recursivePrint(L[1:])

# print(recursivePrint(tempBoard))
# print(len(tempBoard))

# Helper function for print2dList.
# This finds the maximum length of the string
# representation of any item in the 2d list
def maxItemLength(a):
    maxLen = 0
    for row in range(len(a)):
        for col in range(len(a[row])):
            maxLen = max(maxLen, len(repr(a[row][col])))
    return maxLen

def print2dList(a):
    if a == []:
        print([])
        return
    print()
    rows, cols = len(a), len(a[0])
    maxCols = max([len(row) for row in a])
    fieldWidth = max(maxItemLength(a), len(f'col={maxCols-1}'))
    rowLabelSize = 5 + len(str(rows-1))
    rowPrefix = ' '*rowLabelSize+' '
    rowSeparator = rowPrefix + '|' + ('-'*(fieldWidth+3) + '|')*maxCols
    print(rowPrefix, end='  ')
    # Prints the column labels centered
    for col in range(maxCols):
        print(f'col={col}'.center(fieldWidth+2), end='  ')
    print('\n' + rowSeparator)
    for row in range(rows):
        # Prints the row labels
        print(f'row={row}'.center(rowLabelSize), end=' | ')
        # Prints each item of the row flushed-right but the same width
        for col in range(len(a[row])):
            print(repr(a[row][col]).center(fieldWidth+1), end=' | ')
        # Prints out missing cells in each column in case the list is ragged
        missingCellChar = chr(10006)
        for col in range(len(a[row]), maxCols):
            print(missingCellChar*(fieldWidth+1), end=' | ')
        print('\n' + rowSeparator)
    print()

# Let's give the new function a try!
a = [ [ 1, -1023, 3 ] , [ 4, 5, 678 ] ]
b = [ [123, 4567, 891011], [567890, 'ABC'], ['Amazing!', True, '', -3.14, None]]
print2dList(tempBoard)