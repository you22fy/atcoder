H,W = map(int,input().split())
S = [list(input().split()) for _ in range(H)]
T = [list(input().split()) for _ in range(H)]


flag = True

new_S = []
new_T = []

for i in range(W):
    tmp_S = []
    tmp_T = []
    for j in range(H):
        tmp_S.append(S[j][0][i])
        tmp_T.append(T[j][0][i])
    new_S.append(tmp_S)
    new_T.append(tmp_T)

for lst in new_S:
    print(lst)
    if lst in new_T:
        pass
    else:
        flag = False
        break

if flag:
    print("Yes")
else:
    print("No")


