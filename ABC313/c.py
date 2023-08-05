n = int(input())
a_lst = list(map(int, input().split()))
a_lst = sorted(a_lst)
c = 0


while max(a_lst) - min(a_lst) > 1:
    diff = (max(a_lst) - min(a_lst))//2

    a_lst[-1] -= diff
    a_lst[0] += diff
    if a_lst[-1] < a_lst[-2]:
        a_lst[-1], a_lst[-2] = a_lst[-2], a_lst[-1]
    if a_lst[0] > a_lst[1]:
        a_lst[0], a_lst[1] = a_lst[1], a_lst[0]
    c+=diff
print(c)

