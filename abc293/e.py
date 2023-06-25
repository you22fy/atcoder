a,x,m = map(int,input().split())
def pow_k(x, n):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2

    return K * x

t_sum = 0
for i in range(x):
    t_sum += pow_k(a,i)%m
print(t_sum%m)

