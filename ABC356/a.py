"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, l, r = map(int, input().split())
    ans = list(range(1, l))
    ans += reversed(list(range(l, r + 1)))
    ans += list(range(r + 1, n + 1))
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()
