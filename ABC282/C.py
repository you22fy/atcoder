N = int(input())
S = str(input())

isIn = [False,False]
ans =""
S = S.replace(",",".")

mode = False

for i in S:
    if i == '"':
        mode = not mode

    if mode:
        if i == ".":
            ans+=","
        else:
            ans+=i
    else:
        ans+=i
print(ans)

