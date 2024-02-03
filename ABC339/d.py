from collections import deque


N = int(input())
grid = []

for _ in range(N):
    grid.append(input())

players = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'P':
            players.append((i, j))
start = tuple(players)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()


q = deque([((start[0], start[1]), 0)])  # (状態, 操作回数)
visited.add(start)

ans = -1

while q:
    (p1, p2), count = q.popleft()
    if p1 == p2:
        ans = count
        break

    for dx, dy in directions:
        np1, np2 = (p1[0] + dx, p1[1] + dy), (p2[0] + dx, p2[1] + dy)
        if 0 <= np1[0] < N and 0 <= np1[1] < N and grid[np1[0]][np1[1]] != '#':
            if not (0 <= np2[0] < N and 0 <= np2[1] < N and grid[np2[0]][np2[1]] != '#'):
                np2 = p2
        else:
            np1 = p1
            if not (0 <= np2[0] < N and 0 <= np2[1] < N and grid[np2[0]][np2[1]] != '#'):
                np2 = p2

        new_state = (np1, np2)
        if new_state not in visited:
            visited.add(new_state)
            q.append((new_state, count + 1))

print(ans)
