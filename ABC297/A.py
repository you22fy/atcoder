n, d = map(int, input().split())
lst = list(map(int, input().split()))
ans = -1
for i in range(n-1):
    if lst[i+1] - lst[i] <=d:
        ans = lst[i+1]
        break
print(ans)