h,w = map(int, input().split())
a_lst = []
a_lst = [input() for _ in range(h)]
b_lst = []
b_lst = [input() for _ in range(h)]

a_row_set = set(a_lst)

for i in a_row_set:
    if a_lst.count(i) == b_lst.count(i):
        print('Yes')
    else:
        print('No')