import sys
m = int(input())
s1 = list(input())
s2 = list(input())
s3 = list(input())

s_intersection = set(s1).intersection(set(s2)).intersection(set(s3))
if len(s_intersection) == 0:
    print(-1)
    sys.exit
t = 0
s1_stop =set()
s2_stop =set()
s3_stop =set()

while True:
    hit = (t % m)
    s1_stop.add(s1[hit])
    s2_stop.add(s2[hit])
    s3_stop.add(s3[hit])
    stop_intersection = s1_stop.intersection(s2_stop).intersection(s3_stop)
    print(stop_intersection)
    if len(stop_intersection) == 1:
        break
    t += 1
print(t)