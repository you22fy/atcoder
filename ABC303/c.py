n,m,h,k = map(int, input().split())
s = input()
items = {tuple(map(int, input().split())) for _ in range(m)}

pos = [0,0]

for i in s:
    if i == 'R':
        pos[0] += 1
    elif i == 'L':
        pos[0] -=1
    elif i == 'U':
        pos[1] += 1
    else:
        pos[1] -=1
    h -= 1
    if h  == -1:
        break
    elif h<k and tuple(pos) in items :
        items.remove(tuple(pos))
        h = k

if(h >= 0):
    print('Yes')
else:
    print('No')
