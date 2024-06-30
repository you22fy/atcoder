"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n = int(input())
    a = list(map(int, input().split()))
    colors = [i for i in range(1, n + 1)]
    ans = 0
    for part_i in range(0, 2 * n - 2):
        part = a[part_i : part_i + 3]
        # print(part)
        for color in colors:
            if part[0] == color and part[2] == color:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
