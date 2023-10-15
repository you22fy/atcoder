import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
# https://qiita.com/rudorufu1981/items/c6bc5e4d72cfe1cb7f14

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
n = I()

while n %2 == 0:
    n = n // 2
while n % 3 == 0:
    n = n//3

if n == 1:
    print('Yes')
else:
    print('No')