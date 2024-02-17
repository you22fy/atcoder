def main():
    h, w, n = map(int, input().split())
    t = list(input())

    s = [list(input()) for _ in range(h)]

    operations_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    ans = 0
    for row in range(h):
        for col in range(w):
            if s[row][col] == "#":
                continue
            isSuccess = True
            current_row = row
            current_col = col
            for op in t:
                current_row = current_row + operations_map[op][0]
                current_col = current_col + operations_map[op][1]
                if (
                    0 <= current_row < h
                    and 0 <= current_col < w
                    and s[current_row][current_col] == "."
                ):
                    continue
                else:
                    isSuccess = False
                    break
            if isSuccess:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
