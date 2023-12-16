s = input()
t = input()

s1, s2 = s[0], s[1]
t1, t2 = t[0], t[1]

vertices = ['A', 'B', 'C', 'D', 'E']

idx1_s = vertices.index(s1)
idx2_s = vertices.index(s2)
distance_s = abs(idx1_s - idx2_s)
distance_s = min(distance_s, 5 - distance_s)

idx1_t = vertices.index(t1)
idx2_t = vertices.index(t2)
distance_t = abs(idx1_t - idx2_t)
distance_t = min(distance_t, 5 - distance_t)

ans = "Yes" if distance_s == distance_t else "No"
print(ans)
