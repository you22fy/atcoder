s = input()
n = len(s)
m = 1
for i in range(n):
    for j in range(i+1, n):
        tgt = s[i:j+1]
        # print(i,j,tgt)
        if tgt == tgt[::-1]:
            m = max(m, len(tgt))
print(m)