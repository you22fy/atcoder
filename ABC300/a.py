n,a,b = map(int, input().split())
num_list = list(map(int, input().split()))

sum = a+b
for id, item in enumerate(num_list):
    if item == sum:
        print(id+1)
