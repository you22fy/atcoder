n = int(input())
lst = []
for _ in range(n):
    lst.append(input())
flag =False

for i in range(n):
    for j in range(n):
        tgt = lst[i] + lst[j]
        if i != j and tgt == tgt[::-1]:
            flag = True
            break
    else:
        continue
    break

if flag:
    print("Yes")
else:
    print("No")