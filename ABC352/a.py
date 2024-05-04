"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    _, x, y, z = map(int, input().split())
    l, r = min(x, y), max(x, y)
    if l <= z <= r:
        print("Yes")
    else:
        print("No")
    return


if __name__ == "__main__":
    main()
