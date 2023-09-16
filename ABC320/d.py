n,m = map(int, input().split())
dic = {}
for i in range(n):
    dic[i] = "decidable"
dic[0] = (0, 0)
a_lst = []
b_lst = []
positions = []
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a_lst.append(a)
    b_lst.append(b)
    positions.append((x,y))

