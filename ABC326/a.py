x, y = map(int, input().split())

dif = y - x
if (dif < 0  and abs(dif) >3 ) or (dif > 0 and abs(dif) > 2):
    print('No')
else:
    print('Yes')