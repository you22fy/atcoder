"""
 _____ _     _____
|_   _| |   | ____|
  | | | |   |  _|
  | | | |___| |___
  |_| |_____|_____|
n,q = map(int, input().split())
s = list(input())
questions = [list(map(int, input().split())) for _ in range(q)]

for question in questions:
    t_s = s[question[0]-1:question[1]]
    t_count = 0
    for wi in range(len(t_s) - 1):
        if t_s[wi] == t_s[wi+1]:
            t_count += 1
    print(t_count)
"""
"""
 _____ _     _____
|_   _| |   | ____|
  | | | |   |  _|
  | | | |___| |___
  |_| |_____|_____|

n,q = map(int, input().split())
s = list(input())
questions = [list(map(int, input().split())) for _ in range(q)]

pairs = [(w, w+1) for w in range(n-1) if s[w] == s[w+1]]

for question in questions:
    counter = 0
    for pair in pairs:
        if question[0]-1 <= pair[0] and pair[1] <= question[1]-1:
            counter += 1
    print(counter)
"""

"""
    _    ____
   / \  / ___|
  / _ \| |
 / ___ \ |___
/_/   \_\____|
"""
n, q = map(int, input().split())
s = input()
questions = [list(map(int, input().split())) for _ in range(q)]

pairs = [0] * n
for i in range(1, n):
    pairs[i] = s[i] == s[i - 1]

cumulative_pairs = [0] * (n + 1)
for i in range(1, n + 1):
    cumulative_pairs[i] = cumulative_pairs[i - 1] + pairs[i - 1]

for question in questions:
    result = cumulative_pairs[question[1]] - cumulative_pairs[question[0]]
    print(result)
