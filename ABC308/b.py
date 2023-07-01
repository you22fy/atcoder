n, m = map(int, input().split())
ate = input().split()
color = input().split()
color = [""] + color
price = map(int, input().split())

order_dic = dict(zip(color, price))
ans = 0
for i in ate:
    if i in color:
        ans += order_dic[i]
    else:
        ans += order_dic[""]

print(ans)