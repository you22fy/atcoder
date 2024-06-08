"""python_template"""

import sys

sys.setrecursionlimit(10**9)


def gen(n: int):
    if n == 0:
        return ["#"]
    smaller_carpet = gen(n - 1)
    size = len(smaller_carpet)
    new_size = size * 3
    carpet = [["." for _ in range(new_size)] for _ in range(new_size)]

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for x in range(size):
                for y in range(size):
                    carpet[i * size + x][j * size + y] = smaller_carpet[x][y]

    return ["".join(row) for row in carpet]


def main():
    n = int(input())
    ans = gen(n)
    for row in ans:
        print(row)


if __name__ == "__main__":
    main()
