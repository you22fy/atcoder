n,m,k = map(int, input().split())
graph = [[-1 for _ in range(n)] for _ in range(n)]

for i in range(m):
    v1,v2, w1 = map(int, input().split())
    graph[v1-1][v2-1] = w1

for row in graph:
    print(row)