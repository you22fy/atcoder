x,y,n = map(int, input().split()) 

sum1 = 0
sum2 = 0

tmp = n//3
sum1+=tmp*y

tmp = n%3
sum1+=tmp*x

sum2 = x*n
if sum1>sum2:
    print(sum2)
else:
    print(sum1)