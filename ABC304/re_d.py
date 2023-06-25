w, h = map(int, input().split())
n = int(input())

fruits_pos = [tuple(map(int, input().split())) for _ in range(n)]

a = int(input())
cut_y = [0]
cut_y += list(map(int, input().split()))
cut_y += [w]

b = int(input())
cut_x = [0]
cut_x += list(map(int, input().split()))
cut_x += [h]

for f in fruits_pos:
    for 
