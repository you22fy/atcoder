n = int(input())
d = list(map(int, input().split()))
ans = 0
for m in range(1, n+1):
    for day in range(1, d[m-1]+1):
        numbers = list(str(m)) + list(str(day))

        if len(set(numbers)) == 1:
            ans += 1
print(ans)
