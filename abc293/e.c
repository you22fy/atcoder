#include <stdio.h>
#include <math.h>
int main(){
    int a,x,m;

    a = scanf("%d", &a);
    x = scanf("%d", &x);
    m = scanf("%d", &m);

    printf("%d,%d,%d",a,x,m);
    int child = 1-pow(a,x);
    int mom = 1-a;

    int sum = child/mom;

    int ans = sum%m;

    printf("%d\n", ans);
}