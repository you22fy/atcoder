# TLE ブルートフォース
n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        arr_i = arr[i]
        arr_j = arr[j]
        sim_count = 0
        for arr_i_item , arr_j_item in zip(arr_i, arr_j):
            if arr_i_item == arr_j_item:
                sim_count += 1
        ans += sim_count % 2
print(ans)