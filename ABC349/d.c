#include <stdio.h>

unsigned long long nextSegment(unsigned long long l, unsigned long long R) {
    if (l >= R) return R;
    unsigned long long power = 1;
    // l に最も近い2のべき乗
    while (power <= l) power <<= 1;
    power >>= 1;
    if (l + power > R) power >>= 1;
    return l + power;
}

void printGoodSequences(unsigned long long L, unsigned long long R) {
    unsigned long long l = L;
    int count = 0;

    unsigned long long segments[100][2];

    while (l < R) {
        unsigned long long r = nextSegment(l, R);
        if (r > R) r = R;
        segments[count][0] = l;
        segments[count][1] = r;
        count++;
        l = r;
    }

    printf("%d\n", count);
    for (int i = 0; i < count; i++) {
        printf("%llu %llu\n", segments[i][0], segments[i][1]);
    }
}

int main() {
    unsigned long long L, R;
    scanf("%llu %llu", &L, &R);
    printGoodSequences(L, R);
    return 0;
}
