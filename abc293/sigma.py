import math
a,x,m = map(int,input().split())

sum = (1-pow(a,x-1))/math.log(a)
print(sum%m)