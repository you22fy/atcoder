board = []
for _ in range(8):
    board.append(list(map(str, input().split())))
dic = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h'}

for i in range(8):
    for j in range(8):
        if board[i][0][j] == '*':
            print(str(dic[j])+(str(8-i)))
