def main():
    n ,q = map(int, input().split())
    s = list(input())

    for _ in range(q):
        i, l, r = map(int, input().split())
        if i == 1:
            part = s[l : r + 1]
            
        else:
            pass


if __name__ == '__main__':
    main()