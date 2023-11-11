"""
 _____ _     _____
|_   _| |   | ____|
  | | | |   |  _|
  | | | |___| |___
  |_| |_____|_____|

s = input()

while 'ABC' in s:
    idx = s.find('ABC')
    s = s[:idx] + s[idx+3 :]

print(s)
"""

s = input()

stack = []
for char in s:
    stack.append(char)
    if len(stack) >= 3 and ''.join(stack[-3:]) == "ABC":
        stack.pop()
        stack.pop()
        stack.pop()
print(''.join(stack))
