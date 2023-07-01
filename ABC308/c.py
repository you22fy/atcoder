n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
rates = []
base = 1000000000
for id, res in enumerate(lst):
    if res[0] == 0 and res[1] != 0:
        rates.append([id+1, 0])
    elif res[0] != 0 and res[1] ==0:
        rates.append([id+1, base])
    else:
        rates.append([id+1, base*res[0]/(res[0]+res[1])])

sorted_rates = sorted(rates, key=lambda x: (-x[1], x[0]))

ans = []
for i in sorted_rates:
    ans.append(str(i[0]))

print(*ans)

