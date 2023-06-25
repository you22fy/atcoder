n, a, b = map(int,input().split())
s = str(input())
def check_rotation(txt):
    rev = txt[::-1]
    if txt == rev:
        return True
    else:
        return False
s_set = set()
for i in s:
    s_set.add(i)

word_dic = dict()

for i in s_set:
    word_dic[i] = s.count(i)


