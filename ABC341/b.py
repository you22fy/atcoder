n = int(input())

a = list(map(int, input().split()))

st = [list(map(int, input().split())) for _ in range(n - 1)]
s = list(map(lambda x: x[0], st))
t = list(map(lambda x: x[1], st))

for i in range(n-1):
    if a[i] >= s[i]:
        exchange =  a[i] // s[i]
        a[i] -= exchange * s[i]
        a[i+1] += exchange * t[i]

print(a[-1])