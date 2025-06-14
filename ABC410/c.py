def main():
    n, q = map(int, input().split())
    queries = [input().split() for _ in range(q)]

    a = [i+1 for i in range(n)]
    offset = 0

    for query in queries:
        match query[0]:
            case '1':
                p, x = int(query[1]), int(query[2])
                a[(p - 1 + offset) % n] = x
            case '2':
                p = int(query[1])
                print(a[(p - 1 + offset) % n])
            case '3':
                k = int(query[1])
                offset = (offset + k) % n

if __name__ == "__main__":
    main()
