n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
l = int(input())
c = list(map(int, input().split()))
q = int(input())
x = list(map(int, input().split()))

st = set()

for i in a:
    for j in b:
        for k in c:
            st.add(i + j + k)

for i in x:
    if i in st:
        print('Yes')
    else:
        print('No')