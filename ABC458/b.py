def main():
    h, w = map(int, input().split())
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for hi in range(h):
        row = []
        for wi in range(w):
            cnt = 0
            for dh, dw in dirs:
                nh, nw = hi + dh, wi + dw
                if 0 <= nh < h and 0 <= nw < w:
                    cnt += 1
            row.append(cnt)
        print(*row)


if __name__ == "__main__":
    main()
