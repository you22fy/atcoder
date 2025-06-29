def main():
    n = int(input())
    pairs = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    for pair in pairs:
        a, b = pair[0], pair[1]
        if b > a:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
