n = int(input())
a_lst = list(map(int, input().strip().split()))

max_a = max(a_lst)
min_a= min(a_lst)
c = 0
while max_a - min_a >1:
    diff = (max_a - min_a)//2
    a_lst[a_lst.index(max_a)] -= diff
    a_lst[a_lst.index(min_a)] += diff
    max_a = max(a_lst)
    min_a= min(a_lst)
    c += diff
print(c - diff)
