n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))

l, r = 0, 0
ans = 0

# スライディんグウィンドウ
while r < n:
    while r < n and a[r] - a[l] < m:
        r += 1
    ans = max(ans, r - l)
    while l < n - 1 and a[l] == a[l + 1]:
        l += 1
    l += 1

print(ans)
