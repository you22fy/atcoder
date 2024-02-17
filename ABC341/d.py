import math


def main():
    n, m, k = map(int, input().split())
    left, right = 1, k * max(n, m)
    while left < right:
        mid = (left + right) // 2
        # nかmの一方で割り切れる個数 = (nの倍数の個数) + (mの倍数の個数) - (nかつmの倍数の個数) * 2
        count = (mid // n) + (mid // m) - 2 * (mid // (n * m // math.gcd(n, m)))
        if count < k:
            left = mid + 1
        else:
            right = mid

    print(right)


if __name__ == "__main__":
    main()
