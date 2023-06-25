n = int(input())
a_lst = list(map(int, input().split()))
isCalled = [False for _ in range(len(a_lst))]
ans = []
for i,j in enumerate(a_lst):
    if isCalled[i] == False:
        isCalled[j-1] = True
for i in range(len(a_lst)):
    if isCalled[i] == False:
        ans.append(i+1)
print(isCalled.count(False))
print(*ans)