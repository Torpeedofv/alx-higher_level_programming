#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 96 < ord(i) < 123:
            i = chr(ord(i) - 32)
        else:
            i = chr(ord(i) - 0)
        print('{}'.format(i), end='')
    print()
