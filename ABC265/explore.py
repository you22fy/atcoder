# n,m,t = map(int, input().split()) 
# room_list= list(map(int, input().split()))

# b_list = []
# for i in range(m):
#     b_list.append(list(map(int,input().split())))
# bonus = 0

# for i in range(n-1):
#     t-=room_list[i]
#     if bonus<m:
#         if b_list[bonus][0] == i+1:
#             t+=b_list[bonus][1]
#             bonus+=1

# if t>=0:
#     print('Yes')
# else:
#     print('No')
N,M,T=map(int,input().split())
A=[0]+list(map(int,input().split()))
bonus=[0]*(N+1)
for _ in range(M):
    x,y=map(int,input().split())
    bonus[x]=y
print(N,M,T,A,bonus)

# i -> i+1
for i in range(1,N):
    if T<=A[i]:
        print("No")
        exit()
    T-=A[i]
    T+=bonus[i+1]

print("Yes")