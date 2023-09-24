def check321(num):
    while num >= 10:
        if num % 10 >= (num // 10) % 10:
            return False
        num //= 10
    return True


k = int(input())

num = 0
i = 1
while True:
    if num == k:
        break

    if check321(i):
        num += 1
    i += 1
print(i-1)

