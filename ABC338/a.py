import bisect,collections,copy,heapq,itertools,math,string
import sys




s = input()

if s[0].isupper():
    for i in s[1:]:
        if i.islower():
            continue
        else:
            print("No")
            exit()
else:
    print("No")
    exit()
print("Yes")