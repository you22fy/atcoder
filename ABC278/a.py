N,K = map(int,input().split())

lst = list(map(int, input().split()))
l = len(lst)
del lst[:K]

for i in range(K):
    if i < l:
        lst.append(0)

print(*lst)
