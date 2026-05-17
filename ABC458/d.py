import heapq


def main():
    x = int(input())
    q = int(input())
    lower, upper = [], []

    heapq.heappush(lower, -x)

    for _ in range(q):
        a, b = map(int, input().split())
        for num in (a, b):
            if not lower or num <= -lower[0]:
                heapq.heappush(lower, -num)
            else:
                heapq.heappush(upper, num)
            if len(lower) > len(upper) + 1:
                heapq.heappush(upper, -heapq.heappop(lower))
            elif len(upper) > len(lower):
                heapq.heappush(lower, -heapq.heappop(upper))
        med = -lower[0] if len(lower) > len(upper) else upper[0]
        print(med)


if __name__ == "__main__":
    main()
