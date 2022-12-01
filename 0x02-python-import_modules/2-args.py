#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    args = 1
    if argc <= 1:
        print('{} arguments.'.format(argc - 1))
    elif argc == 2:
        print('{} argument:'.format(argc - 1))
    else:
        print('{} arguments:'.format(argc - 1))
    while args < argc:
        print('{}: {}'.format(args, sys.argv[args]))
        args += 1
