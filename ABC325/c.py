H, W = map(int, input().split())
S = [input() for _ in range(H)]

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, 1, -1]

visited = [[False] * W for _ in range(H)]

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        for d in range(8):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and S[nx][ny] == '#':
                stack.append((nx, ny))

count = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#' and not visited[i][j]:
            count += 1
            dfs(i, j)

print(count)
