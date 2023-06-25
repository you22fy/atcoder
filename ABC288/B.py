n,k = map(int, input().split())
str_lst = [str(input()) for _ in range(n)]
ans_lst = str_lst[:k]
ans_lst.sort()

for i in ans_lst:
    print(i)
