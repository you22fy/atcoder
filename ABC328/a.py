n,x = map(int, input().split())
s = list(map(int, input().split()))
a = 0
for p in s:
    if p <= x:
        a += p

print(a)