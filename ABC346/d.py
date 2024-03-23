def min_cost_to_good_string(N, S, C):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N):
        if S[i] != S[i - 1]:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(dp[i], dp[i - 1] + C[i - 1])

    return dp[N - 1]

N = int(input())
S = input()
C = list(map(int, input().split()))

min_cost = min_cost_to_good_string(N, S, C)
print(min_cost)

