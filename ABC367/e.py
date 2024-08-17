"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n, k = map(int, input().split())
    x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    final_positions = list(range(n))

    for _ in range(k):
        new_positions = [0] * n
        for i in range(n):
            new_positions[i] = final_positions[x[i] - 1]
        final_positions = new_positions

    result = [0] * n
    for i in range(n):
        result[final_positions[i]] = a[i]

    print(*result)


if __name__ == "__main__":
    main()
