import heapq
import sys

input = sys.stdin.read


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.par[rx] = ry
                self.size[ry] += self.size[rx]
            else:
                self.par[ry] = rx
                self.size[rx] += self.size[ry]
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] += 1


def kruskal(n, edges):
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []
    for c, u, v in edges:
        if not uf.find(u) == uf.find(v):
            uf.union(u, v)
            mst_weight += c
            mst_edges.append((c, u, v))
    return mst_weight, mst_edges


def main():
    data = input().split()
    idx = 0
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2
    edges = []

    for _ in range(N - 1):
        a = int(data[idx]) - 1
        b = int(data[idx + 1]) - 1
        c = int(data[idx + 2])
        edges.append((c, a, b))
        idx += 3

    edges.sort()
    mst_weight, mst_edges = kruskal(N, edges)

    result = []
    for _ in range(Q):
        u = int(data[idx]) - 1
        v = int(data[idx + 1]) - 1
        w = int(data[idx + 2])
        idx += 3
        # Add the new edge to the edges list and sort
        heapq.heappush(edges, (w, u, v))

        # Apply Kruskal's algorithm again
        mst_weight, mst_edges = kruskal(N, edges)

        result.append(mst_weight)

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
