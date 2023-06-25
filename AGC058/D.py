import math

num_list = list(map(int, input().split()))

graph = [
    ['A','A',0],
    ['B','B',1],
    ['C','C',2],
    ['A','C',3],
    ['C','B',4],
    ['B','A',5]
]
sum = 0

use_list = num_list
ans_list = []

# TODO 全部の組み合わせを生成する
while use_list[0]!=0 and use_list[1]!=0 and use_list[2]!=0:
    
# TODO illegal_listを含んでいるものの個数減らす。



print(sum%998244353)
