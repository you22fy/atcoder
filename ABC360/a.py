'''python_template'''

import sys

sys.setrecursionlimit(10**9)


def main():
    '''main function'''
    s = input()
    
    ri = s.index('R')
    mi = s.rindex('M')
    if ri < mi:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()
