import bisect,collections,copy,heapq,itertools,math,string
import sys

s= input()
word = set(list(s))

word_map = {k:0 for k in word}

word_map = dict(sorted(word_map.items(), key=lambda x:x[0]))

for i in s:
    word_map[i] += 1

max_value = max(word_map.values())
max_keys = [k for k, v in word_map.items() if v == max_value]
print(max_keys[0])
