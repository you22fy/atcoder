n,m = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))
ans = 0
for i in b_lst:
    ans += a_lst[i-1]
print(ans)