n,t = map(int, input().split())
c_lst = list(map(int, input().split()))
r_lst = list(map(int, input().split()))
cr_lst = [c_lst, r_lst]

m = 0
ans = 0
if t in c_lst:
    for i in range(n):
        if cr_lst[0][i] == t:
            if m <cr_lst[1][i]:
                m = cr_lst[1][i]
                ans = i+1
else:
    t = c_lst[0]
    for i in range(n):
        if cr_lst[0][i] == t:
            if m <cr_lst[1][i]:
                m = cr_lst[1][i]
                ans = i+1
print(ans)