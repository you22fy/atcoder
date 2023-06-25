n, k = map(int, input().split())
s = str(input())
ans = ""
cnt = 0
flag = True
for id, w in enumerate(s):
    if w == 'o' and flag:
        ans += 'o'
        cnt += 1
    else:
        ans+='x'

    if cnt == k:
        flag = False

print(ans)