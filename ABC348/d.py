# TLE(DFS)
"""
. : 空きマス。
# : 障害物。
S : 空きマスかつスタート地点。
T : 空きマスかつゴール地点。
"""
h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
n = int(input())
items = {}  # (R, C) : E

for _ in range(n):
    r, c, e = map(int, input().split())
    items[(r-1, c-1)] = e

for i in range(h):
    for j in range(w):
        if board[i][j] == 'S':
            start = (i, j)
        elif board[i][j] == 'T':
            goal = (i, j)

stack = [(start, 0)]  # (位置, エネルギー)
visited = set()

while stack:
    (x, y), energy = stack.pop()

    if (x, y) == goal:
        print("Yes")
        break

    if ((x, y), energy) in visited:
        continue

    visited.add(((x, y), energy))

    if (x, y) in items and energy < items[(x, y)]:
        energy = items[(x, y)]
        visited = {(pos, en) for pos, en in visited if pos != (x, y)}

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '#' and energy > 0:
            stack.append(((nx, ny), energy - 1))
else:
    print("No")
