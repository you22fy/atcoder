// 再帰回数で引っかかっていると信じてC++に書き直す

#include <iostream>
#include <vector>

using namespace std;

bool fillRec(int h, int w, const vector<pair<int, int>>& tiles, vector<bool>& used, vector<vector<bool>>& board) {
    for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
            if (!board[i][j]) {
                for (int k = 0; k < tiles.size(); ++k) {
                    if (used[k]) continue;

                    int a = tiles[k].first;
                    int b = tiles[k].second;

                    for (int flip = 0; flip < 2; ++flip) {
                        swap(a, b);
                        if (i + a <= h && j + b <= w) {
                            bool canPlace = true;
                            for (int x = i; x < i + a && canPlace; ++x) {
                                for (int y = j; y < j + b && canPlace; ++y) {
                                    if (board[x][y]) canPlace = false;
                                }
                            }

                            if (canPlace) {
                                for (int x = i; x < i + a; ++x) {
                                    for (int y = j; y < j + b; ++y) {
                                        board[x][y] = true;
                                    }
                                }
                                used[k] = true;

                                if (fillRec(h, w, tiles, used, board)) return true;

                                for (int x = i; x < i + a; ++x) {
                                    for (int y = j; y < j + b; ++y) {
                                        board[x][y] = false;
                                    }
                                }
                                used[k] = false;
                            }
                        }
                    }
                }
                return false;
            }
        }
    }
    return true;
}

string mainFunc(int H, int W, int N, const vector<pair<int, int>>& tiles) {
    vector<vector<bool>> board(H, vector<bool>(W, false));
    vector<bool> used(N, false);
    return fillRec(H, W, tiles, used, board) ? "Yes" : "No";
}

int main() {
    int N, H, W;
    cin >> N >> H >> W;

    vector<pair<int, int>> tiles(N);
    for (int i = 0; i < N; ++i) {
        cin >> tiles[i].first >> tiles[i].second;
    }

    cout << mainFunc(H, W, N, tiles) << endl;

    return 0;
}
