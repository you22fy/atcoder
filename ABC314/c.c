#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);

    char s[n+1];
    scanf("%s", s);

    int c[m];
    for (int i = 0; i < m; i++) {
        scanf("%d", &c[i]);
    }

    for (int i = 0; i < m; i++) {
        int p[n];
        char p_word[n+1];
        int p_count = 0;
        
        for (int j = 0; j < n; j++) {
            if (i+1 == c[j]) {
                p[p_count] = j;
                p_word[p_count] = s[j];
                p_count++;
            }
        }
        p_word[p_count] = '\0';  // null-terminate the string

        char last_char = p_word[p_count - 1];
        for (int k = p_count - 1; k > 0; k--) {
            p_word[k] = p_word[k - 1];
        }
        p_word[0] = last_char;

        for (int k = 0; k < p_count; k++) {
            s[p[k]] = p_word[k];
        }
    }

    printf("%s\n", s);
    return 0;
}
