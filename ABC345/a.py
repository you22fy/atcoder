s = input()

if s[0] == '<' and s[-1] == '>':
    for i in s[1:-1]:
        if i != '=':
            print('No')
            exit()
else:
    print('No')
    exit()
print('Yes')