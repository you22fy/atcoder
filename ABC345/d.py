def fill_rec(h, w, tiles, used, board):
    if all(all(row) for row in board):
        return True

    for i in range(h):
        for j in range(w):
            if not board[i][j]:
                for k, (a, b) in enumerate(tiles):
                    if used[k]:
                        continue

                    for _ in range(2):
                        a, b = b, a
                        if i + a <= h and j + b <= w and all(not board[x][y] for x in range(i, i + a) for y in range(j, j + b)):
                            for x in range(i, i + a):
                                for y in range(j, j + b):
                                    board[x][y] = True
                            used[k] = True

                            if fill_rec(h, w, tiles, used, board):
                                return True

                            for x in range(i, i + a):
                                for y in range(j, j + b):
                                    board[x][y] = False
                            used[k] = False

                return False
    return True

def main(H, W, N, tiles):
    board = [[False] * W for _ in range(H)]
    used = [False] * N
    return "Yes" if fill_rec(H, W, tiles, used, board) else "No"

N ,H, W = map(int, input().split())
tiles = [tuple(map(int, input().split())) for _ in range(N)]
print(main(H, W, N, tiles))
