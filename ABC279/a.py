S =str(input())

counter = 0
for i in S:
    if i == 'v':
        counter +=1
    elif i == 'w':
        counter+=2

print(counter)