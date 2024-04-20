def main():
    n, q = map(int, input().split())

    t = list(map(int, input().split()))

    pulled = set()
    for i in range(q):
        if t[i] not in pulled:
            pulled.add(t[i])
        else:
            pulled.remove(t[i])
    print(n - len(pulled))
if __name__ == '__main__':
    main()