#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1, sys
    argc = len(sys.argv) 
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if argc != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>\n', end="")
        sys.exit(1)
    if(operator in "+-*/"):
        if operator is '+':
            print('{} + {} = {}'.format(a, b, add(a, b))
        elif operator is '-':
            print('{} - {} = {}'.format(a, b, sub(a, b))
        elif operator is '*':
            print('{} * {} = {}'.format(a, b, mul(a, b))
        elif operator is '/':
            print('{} / {} = {}'.format(a, b, div(a, b))
        else:
            print('Unknown operator. Available operators: +, -, * and /\n', end="")
            exit(1)
