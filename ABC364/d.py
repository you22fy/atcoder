import bisect


def main():
    """main function"""
    _, q = map(int, input().split())
    a = sorted(map(int, input().split()))

    results = []
    for _ in range(q):
        b, k = map(int, input().split())

        left, right = 0, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            # print(bisect.bisect_right(a, b + mid))
            # print(bisect.bisect_left(a, b - mid))
            count = bisect.bisect_right(a, b + mid) - bisect.bisect_left(a, b - mid)
            if count >= k:
                right = mid
            else:
                left = mid + 1

        results.append(left)

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
