n = int(input())
s = input()
t = input()

flag = False

sim1 = set(['1','l'])
sim2 = set(['0','o'])

for i, j in zip(s,t):
    tmp_set = set([i,j])
    if i == j:
        flag = True
    elif tmp_set == sim1 or tmp_set == sim2:
        flag = True
    else:
        flag = False
        break
if flag:
    print('Yes')
else:
    print('No')


