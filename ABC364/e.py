"""ナップザック問題か・・・・・・"""


def main():
    """main function"""
    n, x, y = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()

    xi, yi = 0, 0
    count = 0
    for ai, bi in zip(a, b):
        count += 1
        xi += ai
        yi += bi
        if x < xi or y < yi:
            print(count)
            exit()
    print(count)


if __name__ == "__main__":
    main()
