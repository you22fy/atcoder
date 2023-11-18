n, m = map(int, input().split())
dic = {i+1 : 0 for i in range(n)}
votes = list(map(int, input().split()))

mx = 0
winner = 0

for v in votes:
    dic[v] += 1
    if mx == dic[v]:
        winner = min(v, winner)
    elif mx < dic[v]:
        mx = dic[v]
        winner = v
    print(winner)
