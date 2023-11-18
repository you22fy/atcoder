n = int(input())
a = set(map(int, input().split()))

mx = max(a)
a.remove(mx)
print(max(a))