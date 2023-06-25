#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

struct Position {
    int x, y;
};

int main() {
    int n, m, h, k;
    std::cin >> n >> m >> h >> k;

    std::vector<Position> items(m);
    for (int i = 0; i < m; i++) {
        std::cin >> items[i].x >> items[i].y;
    }

    Position pos = {0, 0};

    std::string s;
    std::cin >> s;

    for (char i : s) {
        if (i == 'R') {
            pos.x++;
        } else if (i == 'L') {
            pos.x--;
        } else if (i == 'U') {
            pos.y++;
        } else if (i == 'D') {
            pos.y--;
        }
        h--;
        if (h == -1) {
            break;
        }

        if (h < k) {
            auto it = std::find_if(items.begin(), items.end(), [&pos](const Position& item) {
                return item.x == pos.x && item.y == pos.y;
            });

            if (it != items.end()) {
                items.erase(it);
                h = k;
            }
        }
    }

    if (h >= 0) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }

    return 0;
}
