from TilesClass import *
tempBoard = [[Forest(0,0), Field(0, 1), Field(0,2), Mountain(0,3), Field(0,4), Forest(0,5), Field(0,6), Field(0,7), Field(0,8), Field(0,9), Field(0,10)],
             [Field(1,0), Mountain(1,1), Mountain(1,2), Forest(1,3), Forest(1,4), Forest(1,5), Field(1,6), Field(1,7), Forest(1,8), Forest(1,9), Field(1,10)],
             [Forest(2,0), Village(2,1), Forest(2,2), Field(2,3), Forest(2,4), Village(2,5), Forest(2,6), Forest(2,7), Field(2,8), Forest(2,9), Field(2,10)],
             [Mountain(3,0), Forest(3,1), Mountain(3,2), Forest(3,3), Mountain(3,4), Mountain(3,5), Field(3,6), Field(3,7), Village(3,8), Field(3,9), Forest(3,10)],
             [Forest(4,0), Forest(4,1), Field(4,2), Forest(4,3), Mountain(4,4), Field(4,5), Forest(4,6), Field(4,7), Field(4,8), Field(4,9), Mountain(4,10)],
             [Field(5,0), Forest(5,1), Field(5,2), Capital(5,3), Forest(5,4), Mountain(5,5), Mountain(5,6), Forest(5,7),Field(5,8), Forest(5,9), Mountain(5, 10)]]

# def recursivePrint(L):
#     if L == []:
#         return []
#     elif isinstance(L[0], list):
#         return recursivePrint(L[0]) + recursivePrint(L[1:])
#     else:
#         print(L[0], (L[0].x, L[0].y))
#         return [L[0]] + recursivePrint(L[1:])

# print(recursivePrint(tempBoard))