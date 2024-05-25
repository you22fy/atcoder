def main():
    N = int(input())
    intervals = []
    for _ in range(N):
        li, ri = map(int, input().split())
        intervals.append((li, ri))

    starts = []
    ends = []

    for li, ri in intervals:
        starts.append(li)
        ends.append(ri)

    starts.sort()
    ends.sort()

    i = j = 0
    overlap_count = 0

    while i < N and j < N:
        if starts[i] <= ends[j]:
            overlap_count += i - j
            i += 1
        else:
            j += 1

    print(overlap_count)


if __name__ == "__main__":
    main()
