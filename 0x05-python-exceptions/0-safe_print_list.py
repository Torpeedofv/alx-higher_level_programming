#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for element in my_list:
        if count == x:
            break
        count += 1 
        print(element, end="")
    print('')
    return count 
