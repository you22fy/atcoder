s = input()
t = ['A','T', 'C','G']
tmp = 0
ans = 0

for u in s:
    if u in t:
        tmp += 1
    else:
        ans = max(ans,tmp)
        tmp =0
print(ans)

