import pandas as pd
import numpy as np

n,q = map(int,input().split())

lst = []
for i in range(q):
    lst.append(list(map(int,input().split())))


users_lst = [i for i in range(1,n+1)]
data = [[0 for i in range(n)] for j in range(n)]
df = pd.DataFrame(data,index = users_lst)
df.columns = users_lst

for l in lst:
    a = l[1]
    b = l[2]
    if l[0] ==1:
        df.loc[a,b] = 1

    elif l[0] == 2:
        df.loc[a,b] = 0

    elif l[0] == 3:
        if df.loc[a,b] == 1 and df.loc[b,a] ==1:
            print("Yes")
        else:
            print("No")
