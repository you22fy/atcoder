from collections import deque

n, m = map(int, input().split())
x = list(map(int, input().split()))


graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    if i == n:
        graph[i].append(1)
    else:
        graph[i].append(i+1)
print(graph)

dist = [-1] * (n+1)
dist[0] = 0
dist[1] = 0

queue = deque()
queue.append(x[0])

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        queue.append(i)

ans = dist[1:]
print(*ans, sep="\n")

