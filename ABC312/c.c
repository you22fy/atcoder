#include <stdio.h>
#include <stdlib.h>

int compare (const void * a, const void * b) {
   return ( *(int*)b - *(int*)a );
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    
    int a_lst[n];
    for(int i=0; i<n; i++){
        scanf("%d", &a_lst[i]);
    }

    int b_lst[m];
    for(int i=0; i<m; i++){
        scanf("%d", &b_lst[i]);
    }

    qsort(a_lst, n, sizeof(int), compare);
    qsort(b_lst, m, sizeof(int), compare);
    
    int min_a = a_lst[n-1];
    int max_b = b_lst[0];

    int cand;
    
    if(min_a > max_b){
        cand = max_b+1;
    } else {
        int x_a, x_a_cnt, x_b_cnt;
        for(int i=0; i<n; i++){
            x_a = a_lst[i];
            x_a_cnt = n - i;
            x_b_cnt = 0;
            for(int j=0; j<m; j++){
                if(b_lst[j] >= x_a){
                    x_b_cnt += 1;
                } else {
                    break;
                }
            }
            if(x_a_cnt >= x_b_cnt){
                cand = x_a;
                break;
            }
        }
    }
    printf("%d\n", cand);
    return 0;
}
