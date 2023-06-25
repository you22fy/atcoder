import bisect

def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def count_special_numbers(n, primes):
    count = 0

    for a_idx, a in enumerate(primes):
        max_c = int((n // (a**2))**(1/3))
        c_idx = bisect.bisect_right(primes, max_c)

        for b_idx in range(a_idx + 1, len(primes)):
            b = primes[b_idx]
            ab2_limit = n // (a**2 * b)
            c_idx = bisect.bisect_left(primes, ab2_limit, c_idx)

            if c_idx <= b_idx:
                break

            count += (c_idx - b_idx - 1)

    return count

n = int(input())
primes = sieve_of_eratosthenes(n)
result = count_special_numbers(n, primes)
print(result)
