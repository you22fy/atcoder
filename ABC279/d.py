import math
from decimal import Decimal


A,B = map(int,input().split())

x = Decimal((A**(2/3)/(2**(2/3)*B**(2/3)))-1)

if x<=0:
    print(A)
else:
    print(Decimal(Decimal(A/math.sqrt(x+1))+Decimal((x)*B)))

