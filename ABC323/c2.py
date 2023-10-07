n, m = map(int, input().split())
scores = list(map(int, input().split()))
users_result = [list(input()) for _ in range(n)]

question_number_score_dict = {}

for s_id, s in enumerate(scores):
    question_number_score_dict[s_id] = s

question_number_score_dict_sorted = dict(sorted(
    question_number_score_dict.items(), key=lambda x: x[1], reverse=True))
# 現在の点数を取得
users_current_score = [i+1 for i in range(n)]
for p_id, result_line in enumerate(users_result):
    for q_id, q in enumerate(result_line):
        if q != 'x':
            users_current_score[p_id] += question_number_score_dict_sorted[q_id]


mx_score = max(users_current_score)

ans = [0 for _ in range(n)]

for p_id, score in enumerate(users_current_score):
    extra_point = 0
    extra_question_num = 0
    if score != mx_score:
        dif = mx_score - score
        for k, v in question_number_score_dict_sorted.items():
            if extra_point <= dif and users_result[p_id][k] == 'x':
                extra_point += v
                extra_question_num += 1
        print(extra_question_num)
    else:
        print(extra_question_num)
