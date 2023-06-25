n = int(input())
lst = list(map(int, input().split()))
ans = []

for i in range(n-1):
    if abs(lst[i] - lst[i+1]) != 1:
        if lst[i] < lst[i+1]:
            ans.append(lst[i])
            insertion = list(range(lst[i]+1, lst[i+1]))
            for j in insertion:
                ans.append(j)
        elif lst[i] > lst[i+1]:
            ans.append(lst[i])
            insertion = list(range(lst[i]-1, lst[i+1], -1 ))
            for j in insertion:
                ans.append(j)
    else:
        ans.append(lst[i])

ans.append(lst[n-1])

print(*ans)