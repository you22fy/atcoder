lst = list(map(int, input().split()))

ans_flag = True


for i in range(7):
    if lst[i] > lst[i+1]:
        ans_flag = False
    if lst[i] % 25 != 0:
        ans_flag = False
    if not(100 <= lst[i] <= 675):
        ans_flag = False
    if not ans_flag:
        break

if lst[7] % 25 != 0:
    ans_flag = False

print("Yes" if ans_flag else "No")