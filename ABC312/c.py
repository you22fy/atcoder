n, m = map(int, input().split())
a_lst = list(map(int, input().split()))

b_lst = list(map(int, input().split()))

if min(a_lst) > max(b_lst):
    cand = max(b_lst)+1
else:
    a_lst = sorted(a_lst, reverse=True)
    b_lst = sorted(b_lst, reverse=True)
    for i in range(n):
        x_a = a_lst[i]
        x_a_cnt = n - i
        x_b_cnt = 0
        for j in range(m):
            if b_lst[j] >= x_a:
                x_b_cnt += 1
            else:
                break
        if x_a_cnt >= x_b_cnt:
            cand = min(cand, x_a)
print(cand)
