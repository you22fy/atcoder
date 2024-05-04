"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    n = int(input())

    # 全員の身長の合計 - 全員の頭の高さの合計　＋一番頭が高い人の頭の高さ
    total_height = 0  # 体の高さの合計
    total_waste = 0  # 頭の高さの合計
    mx = 0  # 一番頭が高い人の頭の高さ
    for _ in range(n):
        a, b = map(int, input().split())
        total_height += b
        total_waste += b - a
        mx = max(mx, b - a)

    print(total_height - total_waste + mx)


if __name__ == "__main__":
    main()
