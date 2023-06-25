
H,M = map(int,input().split())
flag = False
def check(h,m):
    h = str(h)
    m = str(m)
    if len(h)==1:
        h = "0"+h
    if len(m) == 1:
        m = "0"+m
    a = h[0]
    b = h[1]
    c = m[0]
    d = m[1]

    miss_h = int(a+c)
    miss_m = int(b+d)
    if 0<= miss_h <= 23 and  0<=miss_m <=59:
        return 1
    else:
        return 0

for i in range(H,25,1):
    if i ==H:
        for j in range(M,60,1):
            if check(i,j) == 1:
                print(f"{i} {j}")
                break
        else:
            continue
        break

    elif i < 24:
        for j in range(0,60,1):
            if check(i,j) == 1:
                print(f"{i} {j}")
                break
        else:
            continue
        break

    elif i ==24:
        flag =True
        break

if flag ==True:
    for i in range(24-H):
        for j in range(0,60):
            if check(i,j) == 1:
                print(f"{i} {j}")
                break
        else:
            continue
        break



