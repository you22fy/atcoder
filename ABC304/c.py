import math
n,d = map(int, input().split())
people = []

for _ in range(n):
    people.append(tuple(map(int, input().split())))

# 解答のテーブルを作成する
isInfected = [False for _ in range(n)]

infected = [people[0]]
isInfected[0] = True
i = 0
while i < len(infected):
    tgt = infected[i]
    for id, person in enumerate(people):
        if not isInfected[id]  and math.sqrt((person[0] - tgt[0])**2 + (person[1] - tgt[1])**2) <= d:
            isInfected[id] =True
            infected.append(person)
    i+=1

for i in isInfected:
    if i:
        print('Yes')
    else:
        print('No')