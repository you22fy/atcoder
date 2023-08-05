n, m = map(int, input().split())
lst = []
for i in range(m):
    lst.append(list(map(int, input().split())))
if m == 0:
    print(-1)
    exit()
a_lst = []
b_lst = []
for l in lst:
    a_lst.append(l[0])
    b_lst.append(l[1])

a_set = set(a_lst)
b_set = set(b_lst)
dif = list(a_set - b_set)

if len(dif) >1 :
    print(-1)
else:
    print(dif[0])