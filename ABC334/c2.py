n, k = map(int, input().split())
socks = list(map(int, input().split()))

# 動的計画法の実装
if len(socks) % 2 != 0:
    # 靴下の数は奇数なので、ペアは (n - 1) / 2 組作ることができる
    pairs = (n - 1) // 2
    # DPテーブルの初期化
    dp = [[float('inf')] * (pairs + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    # DPテーブルの更新
    for i in range(1, n + 1):
        for j in range(1, min(i, pairs) + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i - 2][j - 1] + abs(socks[i - 1] - socks[i - 2]))

    # 最小コストの取得
    min_score = min(dp[n])
    print(min_score)

# リストが偶数の場合の処理
else:
    min_score = sum(abs(socks[i] - socks[i + 1]) for i in range(0, len(socks) - 1, 2))
    print(min_score)
