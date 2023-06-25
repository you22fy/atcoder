#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void * a, const void * b) {
    return *(int*)a - *(int*)b;
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int lst[n];
    for(int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
    }

    int keys[n*n][2];
    int index = 0;
    for(int i_l = 1; i_l <= n; i_l++) {
        for(int i_r = 1; i_r <= n; i_r++) {
            if(i_l <= i_r) {
                keys[index][0] = i_l;
                keys[index][1] = i_r;
                index++;
            }
        }
    }

    int nums[n*n][n+1];
    for(int i = 0; i < index; i++) {
        int l = keys[i][0] - 1;
        int r = keys[i][1] - 1;
        int rev_lst[n];
        memcpy(rev_lst, lst, sizeof(int)*n);

        for(int j = 0; j < (r-l+1)/2; j++) {
            int tmp = rev_lst[l+j];
            rev_lst[l+j] = rev_lst[r-j];
            rev_lst[r-j] = tmp;
        }

        int cat_num = 0;
        for(int j = 0; j < n; j++) {
            cat_num = cat_num * 10 + rev_lst[j];
        }

        nums[i][0] = cat_num;
        for(int j = 0; j < n; j++) {
            nums[i][j+1] = rev_lst[j];
        }
    }

    qsort(nums, index, sizeof(int)*(n+1), compare);

    for(int i = 0; i < n; i++) {
        printf("%d ", nums[k-1][i+1]);
    }

    return 0;
}
