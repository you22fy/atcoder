def main():
    n, k = map(int, input().split())
    mod = 10**9

    if n < k:
        print(1)
        return

    dp = [0] * (n + 1)
    cumulative_sum = [0] * (n + 2)

    for i in range(k):
        dp[i] = 1
        cumulative_sum[i + 1] = (cumulative_sum[i] + 1) % mod

    for i in range(k, n + 1):
        dp[i] = (cumulative_sum[i] - cumulative_sum[i - k] + mod) % mod
        cumulative_sum[i + 1] = (cumulative_sum[i] + dp[i]) % mod

    print(dp[n])


if __name__ == "__main__":
    main()
