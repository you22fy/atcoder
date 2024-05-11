"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main() -> None:
    """main function"""
    n = int(input())
    h = list(map(int, input().split()))
    left = h[0]

    for idx, height in enumerate(h[1:]):
        if height > left:
            # print(idx, height, left)
            # left = height
            print(idx + 2)
            return
    print(-1)


if __name__ == "__main__":
    main()
