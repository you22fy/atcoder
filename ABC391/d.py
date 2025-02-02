def bin_search(a, t):
    low, high = 0, len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] <= t:
            low = mid + 1
        else:
            high = mid
    return low


def main() -> None:
    n, w = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    queries = [list(map(int, input().split())) for _ in range(q)]

    # print(n, w)
    # print(blocks)
    # print(q)
    # print(queries)

    cols = [[] for _ in range(w)]
    order = [0] * n

    for i in range(n):
        x, y = blocks[i]
        col_index = x - 1
        cols[col_index].append((y, i))

    for i in range(w):
        cols[i].sort(key=lambda pair: pair[0])

    col_count = [len(cols[i]) for i in range(w)]
    for i in range(w):
        for r, (y, idx) in enumerate(cols[i], start=1):
            order[idx] = r

    if any(c == 0 for c in col_count):
        for _, _ in queries:
            print("Yes")
        return

    r_max = min(col_count)

    m = [0] * (r_max + 1)
    for r in range(1, r_max + 1):
        max_val = 0
        for i in range(w):
            y = cols[i][r - 1][0]
            if y > max_val:
                max_val = y
        m[r] = max_val
    delete_timing = m[1:]  # ブロック消去のタイミング

    for t, a in queries:
        idx = a - 1
        r_count = bin_search(delete_timing, t)
        if order[idx] <= r_count:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
