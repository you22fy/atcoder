n, k = map(int, input().split())
lst = list(map(str, input().split()))

lst_sorted = sorted(lst)
lst_sorted = lst_sorted[::-1]
ans = k
for i in range(k,-1,-1):
    tmp = 0
    if lst_sorted.count(i) < k:
        ans = i
        break

print(ans)
