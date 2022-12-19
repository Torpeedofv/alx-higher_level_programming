#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            count += 1
            print("{}".format(i), end="")
            if count == x:
                raise IndexError
        except IndexError:
            break
    print()
    return count
