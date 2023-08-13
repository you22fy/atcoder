n = int(input())
inp = []
num_of_bet = 0
for i in range(n):
    c_n = int(input())
    num_of_bet = max(num_of_bet, c_n)
    a_lst_n = list(map(int ,input().split()))
    inp.append([c_n, a_lst_n])

x = int(input())
ans = []

for id, item in enumerate(inp):
    if x in item[1]:
        if num_of_bet > item[0]:
            num_of_bet = item[0]
            ans = []
            ans.append(id+1)
        elif num_of_bet == item[0]:
            ans.append(id+1)

if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(*ans)