#include <stdio.h>
#include <stdbool.h>

#define MAX_M 100000

typedef struct {
    int x, y;
} Position;

int main() {
    int n, m, h, k;
    scanf("%d%d%d%d", &n, &m, &h, &k);

    Position items[MAX_M];
    for (int i = 0; i < m; i++) {
        scanf("%d%d", &items[i].x, &items[i].y);
    }

    Position pos = {0, 0};

    char s[MAX_M + 1];
    scanf("%s", s);

    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == 'R') {
            pos.x++;
        } else if (s[i] == 'L') {
            pos.x--;
        } else if (s[i] == 'U') {
            pos.y++;
        } else if (s[i] == 'D') {
            pos.y--;
        }
        h--;
        if (h == -1) {
            break;
        }

        if (h < k) {
            bool isPosInItems = false;
            for (int j = 0; j < m; j++) {
                if (items[j].x == pos.x && items[j].y == pos.y) {
                    isPosInItems = true;
                    // Remove found item
                    for (int k = j; k < m - 1; k++) {
                        items[k] = items[k + 1];
                    }
                    m--;
                    break;
                }
            }
            if (isPosInItems) {
                h = k;
            }
        }
    }

    if (h >= 0) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    return 0;
}
