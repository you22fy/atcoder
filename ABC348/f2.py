# TLE : numpyなら早くあってほしかた
import numpy as np

n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(np.array(list(map(int, input().split()))))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        arr_i = arr[i]
        arr_j = arr[j]
        diff_arr = arr_i - arr_j
        ans  += np.sum(diff_arr == 0) % 2
print(ans)