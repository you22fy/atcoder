import sys
sys.setrecursionlimit(10**8)


class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)

    def add(self, idx, val):
        while idx <= self.n:
            self.data[idx] += val
            idx += idx & -idx

    def sum(self, idx):
        s = 0
        while idx > 0:
            s += self.data[idx]
            idx -= idx & -idx
        return s

    def range_sum(self, left, right):
        return self.sum(right) - self.sum(left-1)


def main():
    n = int(input())
    a = list(map(int, input().split()))

    bit = BinaryIndexedTree(n+1)

    runout = [0]*(n+1)
    s = [0]*(n+1)

    for j in range(1, n+1):
        exhausted_count = bit.sum(j-1)
        adult_j = (j-1) - exhausted_count

        s[j] = a[j-1] + adult_j

        if s[j] < (n - j):
            runout[j] = j + s[j]
        else:
            runout[j] = n + 1

        idx = min(runout[j], n+1)
        bit.add(idx, 1)

    ans = []
    for j in range(1, n+1):
        bj = s[j] - (n - j)
        if bj < 0:
            bj = 0
        ans.append(str(bj))

    print(*ans)


if __name__ == "__main__":
    main()


# 愚直
# def main() -> None:
#     n = int(input())
#     a = list(map(int, input().split()))

#     stones = a[:]

#     for year in range(1, n + 1):  # O(n)
#         adult_count = 0
#         for i in range(year):  # O(n)
#             if stones[i] > 0:
#                 adult_count += 1

#         celebrated_alien = year - 1

#         for i in range(year):  # O(n)
#             if stones[i] > 0 and i != celebrated_alien:
#                 stones[i] -= 1
#                 stones[celebrated_alien] += 1

#     print(*stones)


# if __name__ == "__main__":
#     main()
