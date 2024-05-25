# """python_template"""

# import sys


# def main():
#     """main function"""
#     n, t = map(int, input().split())
#     a = list(map(int, input().split()))
#     patterns = set()
#     # row
#     for i in range(1, 1 + n * n - n + 1, n):
#         patterns.add(frozenset(list(range(i, i + n))))

#     # col
#     for i in range(1, 1 + n):
#         patterns.add(frozenset(list(range(i, n * (n - 1) + n + 1, n))))

#     patterns.add(frozenset(list(range(1, n * n + 1, n + 1))))
#     patterns.add(frozenset(list(range(n, n * n, n - 1))))

#     selected_numbers = set()

#     # 最小のターン数を見つける
#     for turn, number in enumerate(a):
#         selected_numbers.add(number)
#         # パターン一つ一つに対して、選択された数字がパターンを満たしているかチェック
#         for pattern in patterns:
#             if pattern.issubset(selected_numbers):
#                 print(turn + 1)  # ターン数は1ベースで出力
#                 return

#     print(-1)  # ビンゴが達成されなかった場合


# if __name__ == "__main__":
#     main()



def main():
    n, _ = map(int, input().split())
    a = list(map(int, input().split()))
    patterns = []
    count = {}
    index_map = {}

    # 各数字がどのパターンに関連しているかのマッピング
    for i in range(1, n*n + 1):
        index_map[i] = []

    # 横列のパターン
    for i in range(n):
        pattern = []
        for j in range(n):
            index = i * n + j + 1
            pattern.append(index)
            index_map[index].append(len(patterns))
        patterns.append(pattern)

    # 縦列のパターン
    for j in range(n):
        pattern = []
        for i in range(n):
            index = i * n + j + 1
            pattern.append(index)
            index_map[index].append(len(patterns))
        patterns.append(pattern)

    # 対角線のパターン
    diag1 = []
    diag2 = []
    for i in range(n):
        diag1.append(i * n + i + 1)
        index_map[i * n + i + 1].append(len(patterns))
        diag2.append(i * n + (n - i))
        index_map[i * n + (n - i)].append(len(patterns) + 1)
    patterns.append(diag1)
    patterns.append(diag2)

    for i in range(len(patterns)):
        count[i] = 0

    for turn, number in enumerate(a):
        if number in index_map:
            for p in index_map[number]:
                count[p] += 1
                if count[p] == n:
                    print(turn + 1)
                    return

    print(-1)

if __name__ == "__main__":
    main()
