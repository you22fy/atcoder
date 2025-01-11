def main() -> None:
    n, d = list(map(int, input().split()))
    tls = [list(map(int, input().split())) for _ in range(n)]

    for k in range(1, d + 1):
        k_ans = max(map(lambda tl : tl[0] * (tl[1] + k), tls))
        print(k_ans)

if __name__ == "__main__":
    main()
