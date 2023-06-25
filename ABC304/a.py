n = int(input())
name = []
age = []
for i in range(n):
    t1, t2 = input().split()
    name.append(t1)
    age.append(int(t2))

min_id = age.index(min(age))
before_id = name[:min_id]
after_id = name[min_id:]

cat = after_id+before_id
for i in cat:
    print(i)