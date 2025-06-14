def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())

    ans = len([i for i in a if i >= k])
    print(ans)

if __name__ == "__main__":
    main()
