n = int(input())
lst = list(map(int, input().split()))
ans = []
loop = 0
for i in range(n):
    ans.append(str(sum(lst[loop:loop+7])))
    loop += 7

print(*ans)

