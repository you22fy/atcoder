"""Code By Gemini1.5 pro"""

from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    edges = [
        (c, a - 1, b - 1)
        for _ in range(N - 1)
        for a, b, c in [map(int, input().split())]
    ]

    def kruskal(edges):
        uf = UnionFind(N)
        weight_sum = 0
        for c, u, v in edges:
            if not uf.same(u, v):
                uf.union(u, v)
                weight_sum += c
        return weight_sum

    edges.sort()  # 初期辺をソート
    mst_weight = kruskal(edges)

    for _ in range(Q):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        insert_idx = bisect_left(edges, (w, u, v))  # 二分探索で挿入位置を特定
        edges.insert(insert_idx, (w, u, v))  # 新たな辺を挿入
        mst_weight = kruskal(edges)
        print(mst_weight)


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n

    def root(self, x):
        if self.par[x] != x:
            self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.par[y] = x
        self.size[x] += self.size[y]


if __name__ == "__main__":
    main()
