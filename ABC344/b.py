lst = []
while True:
    a = int(input())
    lst.append(a)
    if a == 0:
        break

for item in lst[::-1]:
    print(item)