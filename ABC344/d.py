"""
 ____  _____ ____  
|  _ \|  ___/ ___| 
| | | | |_  \___ \ 
| |_| |  _|  ___) |
|____/|_|   |____/ 
"""

t = input()
n = int(input())

bag = []
for _ in range(n):
    line = input().split()
    bag.append(line[1:])

stack = [('', 0, 0)] # s, i, cost
min_cost = float('inf')

while stack:
    s, i, cost = stack.pop()
    if i == n:
        if s== t:
            min_cost = min(min_cost, cost)
        continue

    stack.append((s, i+1, cost))

    for string in bag[i]:
        new_s = s + string
        stack.append((new_s, i+1, cost+1))
print(min_cost if min_cost != float('inf') else -1)