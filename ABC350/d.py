def main():
    n, m = map(int, input().split())

    relationship = {k : set() for k in range(1, n+ 1)}

    for _ in range(m):
        a, b = map(int, input().split())
        relationship[a].add(b)
        relationship[b].add(a)

    for k, v in relationship.items():
        print(f'{k}: {v}')

    # aとbが友達の時に、aとcを友達にする
    ans = 0
    for a in range(1, n + 1):
        for b in relationship[a]:
            if a < b:
                for c in relationship[b]:
                    if c != a and c not in relationship[a]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
