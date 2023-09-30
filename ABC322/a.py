import sys
n = int(input())
s = input()
for i in range(n-2):
    if s[i] == 'A':
        if s[i+1] == 'B':
            if s[i+2] == 'C':
                print(i+1)
                sys.exit()
print(-1)
