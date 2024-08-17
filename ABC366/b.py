"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n = int(input())
    s = []
    m = 0
    for _ in range(n):
        t = input()
        s.append(t)
        m = max(m, len(t))


if __name__ == "__main__":
    main()
