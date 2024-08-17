'''python_template'''

import sys

sys.setrecursionlimit(10**9)


def main():
    '''main function'''
    n,t,a = map(int, input().split())

    left = n - t -a
    if t > a + left or  a > t + left:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
