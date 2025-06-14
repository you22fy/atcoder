from collections import deque

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))

    visited = [set() for _ in range(n+1)]
    visited[1].add(0)

    queue = deque([(1, 0)])

    while queue:
        v, xor_val = queue.popleft()

        for next_v, weight in graph[v]:
            new_xor = xor_val ^ weight

            if new_xor not in visited[next_v]:
                visited[next_v].add(new_xor)
                queue.append((next_v, new_xor))

    if visited[n]:
        print(min(visited[n]))
    else:
        print(-1)

if __name__ == "__main__":
    main()
