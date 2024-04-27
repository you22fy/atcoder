"""python_template"""


def main():
    """main function"""
    n = int(input())
    grid_a: list = [list(input()) for _ in range(n)]
    grid_b: list = [list(input()) for _ in range(n)]

    for i in range(n):
        la, lb = grid_a[i], grid_b[i]
        for j in range(n):
            if la[j] != lb[j]:
                print(i + 1, j + 1)
                return


if __name__ == "__main__":
    main()
