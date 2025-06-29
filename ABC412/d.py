def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    current_graph = [set() for _ in range(N + 1)]
    for a, b in edges:
        current_graph[a].add(b)
        current_graph[b].add(a)

    current_edges = set()
    for a in range(1, N + 1):
        for b in current_graph[a]:
            if a < b:
                current_edges.add((a, b))

    min_ops = float('inf')

    total_possible_edges = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            total_possible_edges.append((i, j))

    for mask in range(1 << len(total_possible_edges)):
        degree = [0] * (N + 1)
        selected_edges = set()

        for i in range(len(total_possible_edges)):
            if mask & (1 << i):
                a, b = total_possible_edges[i]
                degree[a] += 1
                degree[b] += 1
                selected_edges.add((a, b))

        valid = True
        for i in range(1, N + 1):
            if degree[i] != 2:
                valid = False
                break

        if not valid:
            continue

        edges_to_add = selected_edges - current_edges
        edges_to_remove = current_edges - selected_edges
        ops = len(edges_to_add) + len(edges_to_remove)

        min_ops = min(min_ops, ops)

    print(min_ops)


if __name__ == "__main__":
    main()
