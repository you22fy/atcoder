w, h = map(int, input().split())
n = int(input())

fruits_pos = [tuple(map(int, input().split())) for _ in range(n)]

a = int(input())
cut_y = [0]
cut_y += list(map(int, input().split()))
cut_y += [w]
cut_y_pos =[]
for i in range(len(cut_y) -1):
    cut_y_pos.append(tuple([cut_y[i], cut_y[i+1]]))

b = int(input())
cut_x = [0]
cut_x += list(map(int, input().split()))
cut_x += [h]
cut_x_pos =[]
for i in range(len(cut_x) -1):
    cut_x_pos.append(tuple([cut_x[i], cut_x[i+1]]))

cur_min = 0
cur_max = 0
for pos_x in cut_x_pos:
    for pos_y in cut_y_pos:
        tmp = 0
        for fruit in fruits_pos:
            if pos_y[0] < fruit[0] < pos_y[1] and pos_x[0] < fruit[1] < pos_x[1]:
                tmp += 1
        cut_min = min(cur_min, tmp)
        cur_max = max(cur_max, tmp)
print("{} {}".format(cur_min, cur_max))