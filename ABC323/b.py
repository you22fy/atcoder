n = int(input())
score = {i+1 : 0 for i in range(n)}
for i in range(n):
    result = list(input())
    score[i+1] = result.count('o')

ranking_dic = dict(sorted(score.items(), key = lambda x : x[1], reverse=True))
print(*ranking_dic.keys())