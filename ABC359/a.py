'''python_template'''

import sys

sys.setrecursionlimit(10**9)


def main():
    '''main function'''
    n = int(input())
    cont = 0
    for _ in range(n):
        t = input()
        if t == 'Takahashi':
            cont += 1
    print(cont)
    


if __name__ == '__main__':
    main()
