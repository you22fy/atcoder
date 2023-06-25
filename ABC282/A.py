k = int(input())
ans =""
cnt = 0
i = 65

while cnt <k:
    if i> 90:
        i=65
    ans+=chr(i)
    cnt+=1
    i+=1

print(ans)

