'''python_template'''

import sys

sys.setrecursionlimit(10**9)


def main():
    '''main function'''
    x = input()

    integer = x.split('.')[0]
    decimal = x.split('.')[1]

    new_decimal = ''
    for i, d in enumerate(decimal[::-1]):
        if d == '0':
            continue
        else:
            new_decimal = decimal[::-1][i:][::-1]
            break
    print(integer + '.' + new_decimal if len(new_decimal) > 0 else integer)


if __name__ == '__main__':
    main()
