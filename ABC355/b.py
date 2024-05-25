"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    _, _ = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = A + B
    C.sort()

    # A の要素をセットとして保持
    set_A = set(A)

    # C を走査して、A の要素が連続しているか確認
    for i in range(len(C) - 1):
        if C[i] in set_A and C[i + 1] in set_A:
            print("Yes")
            return

    print("No")


if __name__ == "__main__":
    main()
