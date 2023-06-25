N, X = map(int, input().split())
num_list = [list(map(int, input().split())) for _ in range(N)]
flag = True
# 所有額合計が支払額を下回った場合NO
total = 0
for i in num_list:
    total+=num_list[0]*num_list[1]

if X > total:
    flag = False


if flag:
    print("Yes")
else:
    print("No")