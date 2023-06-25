n = int(input())
s = input()

t_cnt = s.count('T')
a_cnt = s.count('A')
ans = None
if t_cnt > a_cnt:
    ans = 'T'
else:
    ans = 'A'


if t_cnt == a_cnt:
    tmp_a =0;tmp_t = 0
    for i in s:
        if i == 'A':
            tmp_a += 1
        else:
            tmp_t += 1
        if tmp_a == a_cnt:
            ans = 'A'
            break
        elif tmp_t == t_cnt:
            ans = 'T'
            break

print(ans)