N, M = map(int, input().split())
a = str(input()).split()
kanbun =""
for i in range(N):
    kanbun+=str(i+1)
    if str(i+1) in a:
        kanbun+="r"

kanbun = kanbun[::-1]
print(kanbun)

