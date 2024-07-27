"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    _, x, y = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort(reverse=True)
    b = list(map(int, input().split()))
    b.sort(reverse=True)

    xi, yi = 0, 0
    count = 0
    for ai, bi in zip(a, b):
        count += 1
        xi += ai
        yi += bi
        if x < xi or y < yi:
            print(count)
            exit()
    print(count)


if __name__ == "__main__":
    main()
