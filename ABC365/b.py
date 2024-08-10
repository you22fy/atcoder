"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n = int(input())
    a = list(map(int, input().split()))

    sa = sorted(a, reverse=True)
    r2 = sa[1]

    for i in range(n):
        if a[i] == r2:
            print(i + 1)
            break



if __name__ == "__main__":
    main()
