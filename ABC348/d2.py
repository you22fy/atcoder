# TLE(BFS)
from collections import deque

h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
n = int(input())
items = {} # (r,c) : E

for _ in range(n):
    r, c, e = map(int, input().split())
    items[(r-1, c-1)] = e
for i in range(h):
    for j in range(w):
        if board[i][j] == 'S':
            start = (i, j)
        elif board[i][j] == 'T':
            goal = (i, j)

queue = deque([(start, 0)])  # (位置, エネルギー)
visited = set([(start, 0)])

while queue:
    (x, y), energy = queue.popleft()

    if (x, y) == goal:
        print("Yes")
        exit()

    if (x, y) in items and energy < items[(x, y)]:
        new_energy = items[(x, y)]
        if ((x, y), new_energy) not in visited:
            queue.append(((x, y), new_energy))
            visited.add(((x, y), new_energy))

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '#' and energy > 0:
            if ((nx, ny), energy-1) not in visited:
                queue.append(((nx, ny), energy - 1))
                visited.add(((nx, ny), energy-1))
print("No")
