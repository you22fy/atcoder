n, k = map(int, input().split())
socks = (list(map(int, input().split())))

if len(socks) < 2:
    print(0)
    exit()

if len(socks)%2 != 0:
    min_score = float('inf')
    for i in range(len(socks)):
        tmp = socks[:i] + socks[i+1:]
        t_score = sum(abs(tmp[i] - tmp[i + 1]) for i in range(0, len(tmp) - 1, 2))
        min_score = min(min_score, t_score)
    print(min_score)
else:
    min_score = sum(abs(socks[i] - socks[i + 1]) for i in range(0, len(socks) - 1, 2))
    print(min_score)

