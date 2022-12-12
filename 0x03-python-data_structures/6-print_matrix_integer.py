#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j is not i[0]:
                print(' ', end='')
            else:
                print('', end='')
            print('{:d}'.format(j), end='')
        print()
