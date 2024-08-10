"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    s = sum(a)
    # print(f'{s=}')

    # infinityが可能かを最初に判定
    if s <= m:
        print("infinite")
        sys.exit()

    left, right = 0, max(a)
    while right - left > 1:
        mid = (left + right) // 2
        sm = sum(min(x, mid) for x in a)
        if sm <= m:
            left = mid
        else:
            right = mid

    print(left)


if __name__ == "__main__":
    main()
