import sys
n,x = map(int, input().split())
a = list(map(int, input().split()))

ans = -1
for i in range(101):
    b = a.copy()
    b.append(i)
    b = sorted(b)
    tmp_sum = sum(b[1:-1])
    if tmp_sum >= x:
        print(i)
        sys.exit()
print(-1)