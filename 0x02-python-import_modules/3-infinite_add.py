#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sums = 0
    argc = len(sys.argv)
    for i in range(1, argc):
        sums += int(sys.argv[i])
    print('{}'.format(sums))
