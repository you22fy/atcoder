def main() -> None:
    _ = int(input())
    a = list(map(int, input().split()))
    sorted_a = sorted(a, reverse=True)

    cnt = 0
    for bottom_idx, bottom_a in enumerate(sorted_a):
        target = bottom_a / 2

        left = bottom_idx + 1
        right = len(sorted_a)

        while left < right:
            mid = (left + right) // 2
            if sorted_a[mid] <= target:
                right = mid
            else:
                left = mid + 1
        cnt += len(sorted_a) - left

    print(cnt)


if __name__ == "__main__":
    main()
