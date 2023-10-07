"""
このコードは回答に用いないものとする。
C問題の解答は./c2.pyとする
"""

n, m = map(int, input().split())
scores = list(map(int, input().split()))
sorted_scores = sorted(scores, reverse=True)
results = [list(input()) for _ in range(n)]
player_score = [i+1 for i in range(n)]

# print(sorted_scores)
# 現在の点数を取得
for p_id,  result in enumerate(results):
    for q_id, q in enumerate(result):
        if q == 'o':
            player_score[p_id] += scores[q_id]

mx_score = max(player_score)
ans = []

for p_id, score in enumerate(player_score):
    extra_point = 0
    extra_question_num = 0
    if score != mx_score:
        # print(results[p_id])
        dif = mx_score - score
        for ss_id, ss in enumerate(sorted_scores):
            if results[p_id][ss_id] == 'x':
                if extra_point <= dif:
                    extra_point += ss
                    extra_question_num += 1
                else:
                    break
        print(extra_question_num)
    else:
        print(extra_question_num)

