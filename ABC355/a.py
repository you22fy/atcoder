'''python_template'''

import sys

sys.setrecursionlimit(10**9)


def main():
    '''main function'''
    a,b = map(int, input().split())
    if a == b:
        print(-1)
    else:
        s = set([1,2,3])
        rm_ab_set = s - set([a, b])
        print(rm_ab_set.pop())


if __name__ == '__main__':
    main()
