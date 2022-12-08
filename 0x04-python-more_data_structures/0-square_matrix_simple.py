#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squareMat = []
    for i in matrix:
        iMat = []
        for j in i:
            j = j**2
            iMat.append(j)
        squareMat.append(iMat)
    return squareMat
