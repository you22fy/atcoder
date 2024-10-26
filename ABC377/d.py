def main():
    n, m = map(int, input().split())
    lrs = [tuple(map(int, input().split())) for _ in range(n)]

    max_Li = [0] * (m + 2)
    for Li, Ri in lrs:
        if max_Li[Ri] < Li:
            max_Li[Ri] = Li

    for r in range(1, m + 1):
        if max_Li[r] < max_Li[r - 1]:
            max_Li[r] = max_Li[r - 1]

    total_valid_intervals = 0
    for r in range(1, m + 1):
        total_valid_intervals += r - max_Li[r]

    print(total_valid_intervals)


if __name__ == '__main__':
    main()
