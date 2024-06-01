"""python_template"""


def main():
    """main function"""
    n, m, k = map(int, input().split())
    info = []
    for _ in range(m):
        tmp = input().split()
        ci = tmp[0]
        a = [int(x) for x in tmp[1:-1]]
        ri = tmp[-1]
        info.append((ci, a, ri))


if __name__ == "__main__":
    main()
