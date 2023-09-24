s = input()
flg = True
for i in range(len(s) -1 ):
    if int(s[i]) <= int(s[i+1]):
        flg = False
        break
if flg:
    print('Yes')
else:
    print('No')
