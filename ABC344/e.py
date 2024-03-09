# ハッシュテーブルと双方向リスト
from collections import deque

n = int(input())
a = deque(map(int, input().split()))
q = int(input())

hash_tbl = {v: i for i, v in enumerate(a)}

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1], query[2]
        a.insert(hash_tbl[x] + 1, y)
        for i in range(hash_tbl[x] + 1, len(a)):
            hash_tbl[a[i]] = i
    else:
        x = query[1]
        a.remove(x)
        del hash_tbl[x]
        for i, v in enumerate(a):
            hash_tbl[v] = i

print(*a)