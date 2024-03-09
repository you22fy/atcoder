t = input()
n = int(input())

bag = []
for _ in range(n):
    line = input().split()
    bag.append(line[1:])



dp = [[float('inf')] * (len(t) + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(len(t) + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        for string in bag[i - 1]:
            for k in range(j, -1, -1):
                if t[k:j] == string:
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + 1)

ans = dp[n][len(t)] if dp[n][len(t)] != float('inf') else -1
print(ans)
