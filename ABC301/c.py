s = input()
t = input()

cheat = ['a', 't', 'c', 'o', 'd', 'e', 'r']
flag = False
for i in range(len(s)):
    if s[i] == '@' and s[i] in cheat and t[i] in cheat:
        flag = False
    elif s[i] == '@' and s[i] in cheat and t[i] in cheat:
        flag = False
    else:
        
