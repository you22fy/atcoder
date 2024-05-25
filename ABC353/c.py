def main():
    MOD = 1000000000
    n = int(input())
    a = list(map(int, input().split()))

    total_sum = sum(a) % MOD

    res = 0
    for i in range(n-1, -1, -1):
        right_sum = (right_sum + a[i]) % MOD
        if i < n-1:
            res = (res + a[i] * right_sum) % MOD

    print(res)

if __name__ == "__main__":
    main()
