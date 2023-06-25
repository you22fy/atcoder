#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int w, h, n, a, b;
    cin >> w >> h;
    cin >> n;

    vector<pair<int, int>> fruits_pos(n);
    for (int i = 0; i < n; ++i) {
        cin >> fruits_pos[i].first >> fruits_pos[i].second;
    }

    cin >> a;
    vector<int> cut_y(a+2);
    cut_y[0] = 0;
    for (int i = 1; i <= a; ++i) {
        cin >> cut_y[i];
    }
    cut_y[a+1] = w;

    vector<pair<int, int>> cut_y_pos(a+1);
    for (int i = 0; i < a+1; ++i) {
        cut_y_pos[i] = make_pair(cut_y[i], cut_y[i+1]);
    }

    cin >> b;
    vector<int> cut_x(b+2);
    cut_x[0] = 0;
    for (int i = 1; i <= b; ++i) {
        cin >> cut_x[i];
    }
    cut_x[b+1] = h;

    vector<pair<int, int>> cut_x_pos(b+1);
    for (int i = 0; i < b+1; ++i) {
        cut_x_pos[i] = make_pair(cut_x[i], cut_x[i+1]);
    }

    for (auto &pos: cut_x_pos) {
        cout << pos.first << ' ' << pos.second << endl;
    }

    vector<int> num_of_fruits;
    for (auto &pos_x: cut_x_pos) {
        for (auto &pos_y: cut_y_pos) {
            int tmp = 0;
            for (auto &fruit: fruits_pos) {
                if (pos_y.first < fruit.first && fruit.first < pos_y.second 
                && pos_x.first < fruit.second && fruit.second < pos_x.second) {
                    ++tmp;
                }
            }
            num_of_fruits.push_back(tmp);
        }
    }

    auto minmax = minmax_element(num_of_fruits.begin(), num_of_fruits.end());
    cout << *minmax.first << ' ' << *minmax.second << endl;

    return 0;
}
