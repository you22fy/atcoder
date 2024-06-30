def bin_search(array, target, lo=0):
    """bin_search"""
    hi = len(array)
    while lo < hi:
        mid = (lo + hi) // 2
        if array[mid] > target:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    """main function"""
    n, t = map(int, input().split())
    s = input()
    x = list(map(int, input().split()))

    to_right = sorted(
        [(x[i], x[i] + (t + 0.1)) for i in range(n) if s[i] == "1"],
        key=lambda x: x[1],
        reverse=True,
    )
    to_left = sorted(
        [(x[i], x[i] - (t + 0.1)) for i in range(n) if s[i] == "0"],
        key=lambda x: x[1],
    )

    crossed = 0
    left_positions = [pos[0] for pos in to_left]
    left_times = [pos[1] for pos in to_left]

    for tr in to_right:
        index = bin_search(left_positions, tr[0])
        if index < len(to_left):
            count = bin_search(left_times, tr[1], lo=index) - index
            crossed += count

    print(crossed)


if __name__ == "__main__":
    main()
