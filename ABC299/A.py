n = int(input())
s = input()
firstFlag = False
secondFlag = False
st = 0
ed = 0
star = 0
for id, t in enumerate(s):
    if t == '|' and not firstFlag:
        st = id
        firstFlag = True
    elif t=='|' and not secondFlag:
        ed = id
        secondFlag = True

    if t == '*':
        star = id
if st < star and star < ed:
    print('in')
else:
    print('out')