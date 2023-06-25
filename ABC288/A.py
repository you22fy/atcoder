n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int,input().split())))

for lst in num_list:
    print(lst[0]+lst[1])