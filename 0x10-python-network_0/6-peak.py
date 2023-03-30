#!/usr/bin/python3
"""a function that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    for i in range(len(list_of_integers)):
        if (i == 0 or list_of_integers[i] >= list_of_integers[i-1])\
            and (i == len(list_of_integers)-1
                 or list_of_integers[i] >= list_of_integers[i+1]):
            return list_of_integers[i]
