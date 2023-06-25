n,x = map(int, input().split())
lst= list(map(int, input().split()))

st = set(lst)
res = 'No'
for i in lst:
    if i +x in st or i-x in st:
        res = 'Yes'
print(res)