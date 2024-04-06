import heapq
# ダイクストラ法
# 参考: https://nashidos.hatenablog.com/entry/2020/04/07/100508
def dijkstra(start, goal, items):
    energy = [[-1] * w for _ in range(h)]
    energy[start[0]][start[1]] = 0 if start not in items else items[start]
    queue = [(-energy[start[0]][start[1]], start)]  # 優先度付きqueue

    while queue:
        current_energy, (x, y) = heapq.heappop(queue)
        current_energy = -current_energy

        if (x, y) == goal:
            return True

        # 上下左右への移動
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '#' and current_energy > 0:
                new_energy = current_energy - 1
                if (nx, ny) in items:
                    new_energy = max(new_energy, items[(nx, ny)])
                if new_energy > energy[nx][ny]:
                    energy[nx][ny] = new_energy
                    heapq.heappush(queue, (-new_energy, (nx, ny)))

    return False



h, w = map(int, input().split())
board = [list(input()) for _ in range(h)]
n = int(input())
items = {}

for _ in range(n):
    r, c, e = map(int, input().split())
    items[(r-1, c-1)] = e

start = goal = None
for i in range(h):
    for j in range(w):
        if board[i][j] == 'S':
            start = (i, j)
        elif board[i][j] == 'T':
            goal = (i, j)


if dijkstra(start, goal, items):
    print("Yes")
else:
    print("No")
