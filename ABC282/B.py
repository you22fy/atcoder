N, M = map(int,input().split())
str_list = [input() for _ in range(N)]
cnt = 0

def check(a,b):
    flag = True
    for i in range(M):
        if a[i] == "x" and b[i] == "x":
            flag =False

    if flag:
        return True
    else:
        return False


for i in range(N-1):
    for j in range(i+1,N):
        if check(str_list[i],str_list[j]):
            cnt+=1

print(cnt)


