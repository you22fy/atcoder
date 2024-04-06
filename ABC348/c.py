n = int(input())

color_score_map = {}

for i in range(n):
    ai,ci = map(int, input().split())
    if ci in color_score_map.keys(): # エントリがある場合
        color_score_map[ci] = min(color_score_map[ci] , ai)
    else: # エントリの作成
        color_score_map[ci] = ai
    # print(color_score_map)


print(max(color_score_map.values()))
