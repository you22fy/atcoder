s = input()

s_even = list(s[1::2])
if '1' in s_even:
    print('No')
else:
    print('Yes')
