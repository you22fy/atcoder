n, m ,p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(m):
        ans += min(a[i] + b[j], p)

print(ans)


