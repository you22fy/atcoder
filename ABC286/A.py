n,p,q,r,s = map(int, input().split())
lst = list(map(str, input().split()))

lst_head = lst[:p-1]
lst_p_q = lst[p-1:q]
lst_body = lst[q:r-1]
lst_s_r = lst[r-1:s]
lst_tail = lst[s:]
ans_lst =[]
ans_lst.extend(lst_head)
ans_lst.extend(lst_s_r)
ans_lst.extend(lst_body)
ans_lst.extend(lst_p_q)
ans_lst.extend(lst_tail)

print(*ans_lst)

