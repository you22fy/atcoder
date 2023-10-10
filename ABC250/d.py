def isPrime (n):
    for i in range(1, int(n**1/2)):
        if n %(i+1) == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    primes= []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    print(primes)