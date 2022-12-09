#!/usr/bin/python3
def uniq_add(my_list=[]):
    sort = sorted(my_list)
    addList = 0 
    for i in sort:
        if [i] == [i+1]:
            sort.pop([i+1])
    return sort
