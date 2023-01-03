#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newMat = []
    for i in matrix:
        subMat = []
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            multInt = j * 3
            subMat.append(multInt)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        newMat.append(subMat)
    return newMat
