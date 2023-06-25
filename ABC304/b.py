n = str(input())

if len(n) <= 3:
    print(n)
else:
    cut =  len(n) - 3
    remain = n[:len(n) - cut]
    zeros =""
    for i in range(cut):
        zeros += '0'
    print(remain+zeros)