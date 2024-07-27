"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n = int(input())
    s = []
    for _ in range(n):
        s.append(input())
    for i in range(n - 2):
        f1, f2 = s[i], s[i + 1]
        if f1 =='sweet' and f2 == 'sweet':
            print('No')
            exit()
    print('Yes')

if __name__ == "__main__":
    main()
