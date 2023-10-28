n = int(input())

def j(num):
    s_num = str(num)
    prod = int(s_num[0]) * int(s_num[1])
    l = int(s_num[-1])
    return prod == l

for i in range(n, 920):
    if j(i):
        print(i)
        exit()

