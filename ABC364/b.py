"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def main():
    """main function"""
    h, w = map(int, input().split())
    si, sj = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    x = input()
    direction_map = {
        "U": (-1, 0),  # (i,j)
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    pos_i, pos_j = si - 1, sj - 1  # 配列のindexに合わせる
    for xi in x:
        di, dj = direction_map[xi]
        # print(f"縦に{di=}横に{dj=}")
        next_i, next_j = pos_i + di, pos_j + dj
        # print(f"{next_i=} {next_j=}")
        if not (0 <= next_i < h and 0 <= next_j < w):
            continue
        if c[next_i][next_j] == "#":
            continue
        pos_i, pos_j = next_i, next_j

    print(pos_i + 1, pos_j + 1)


if __name__ == "__main__":
    main()
