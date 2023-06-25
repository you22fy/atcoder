n,l=map(int, input().split())
k=int(input())
arr=list(map(int, input().split()))


#先頭に０を末尾にlを挿入
arr.append(l)
arr.insert(0,0)

print(arr)
# print(k)
print(len(arr))

prev = 0
next = k

max_temp = 0

while next<len(arr):
    print(f'prev={ prev } , next={ next }')
    print(f'dif = {arr[next]-arr[prev]}')
    if max_temp<arr[next]-arr[prev]:
        max_temp=arr[next]-arr[prev]
    prev+=1
    next=prev+k


print(max_temp)


