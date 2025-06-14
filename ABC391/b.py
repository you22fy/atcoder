def main() -> None:
    n, m = map(int, input().split())
    s = [input().strip() for _ in range(n)]
    t = [input().strip() for _ in range(m)]

    for a in range(n - m + 1):
        for b in range(n - m + 1):
            found = True
            for i in range(m):
                if s[a + i][b:b + m] != t[i]:
                    found = False
                    break
            if found:
                print(a + 1, b + 1)
                return


if __name__ == "__main__":
    main()
