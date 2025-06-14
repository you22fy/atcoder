# def main():
#     n, h, m = map(int, input().split())
#     ab = [list(map(int, input().split())) for _ in range(n)]

#     dp = [[[-1] * (m + 1) for _ in range(h + 1)] for _ in range(n + 1)]
#     dp[0][h][m] = 0

#     for i in range(n):
#         for j in range(h + 1):
#             for k in range(m + 1):
#                 if dp[i][j][k] == -1:
#                     continue

#                 dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])

#                 # 魔法を使わない
#                 if j >= ab[i][0]:
#                     dp[i + 1][j - ab[i][0]][k] = max(dp[i + 1][j - ab[i][0]][k], dp[i][j][k] + 1)

#                 # 魔法を使う
#                 if k >= ab[i][1]:
#                     dp[i + 1][j][k - ab[i][1]] = max(dp[i + 1][j][k - ab[i][1]], dp[i][j][k] + 1)

#     ans = 0
#     for j in range(h + 1):
#         for k in range(m + 1):
#             ans = max(ans, dp[n][j][k])

#     print(ans)

# if __name__ == "__main__":
#     main()


def main():
    n, h, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]

    dp = [[-1] * (m + 1) for _ in range(h + 1)]
    dp[h][m] = 0

    for i in range(n):
        new_dp = [[-1] * (m + 1) for _ in range(h + 1)]

        for j in range(h + 1):
            for k in range(m + 1):
                if dp[j][k] == -1:
                    continue

                if new_dp[j][k] < dp[j][k]:
                    new_dp[j][k] = dp[j][k]

                # 魔法を使わない
                if j >= ab[i][0]:
                    if new_dp[j - ab[i][0]][k] < dp[j][k] + 1:
                        new_dp[j - ab[i][0]][k] = dp[j][k] + 1

                # 魔法を使う
                if k >= ab[i][1]:
                    if new_dp[j][k - ab[i][1]] < dp[j][k] + 1:
                        new_dp[j][k - ab[i][1]] = dp[j][k] + 1

        dp = new_dp

    ans = 0
    for j in range(h + 1):
        for k in range(m + 1):
            if dp[j][k] > ans:
                ans = dp[j][k]

    print(ans)

if __name__ == "__main__":
    main()
