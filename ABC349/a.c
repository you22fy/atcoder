#include <stdio.h>

int main()
{
    int i, j, k;
    int n;
    scanf("%d", &n);

    int a[n];
    for (i = 0; i < n - 1; i++)
    {
        scanf("%d", &a[i]);
    }

    int minus = 0;
    int plus = 0;

    for (i = 0; i < n - 1; i++)
    {
        if (a[i] < 0)
        {
            minus += a[i];
        }
        else if (a[i] > 0)
        {
            plus += a[i];
        }
    }

    // debug
    // printf("%d %d\n", plus, minus);

    int answer = plus + minus;
    answer *= -1;
    printf("%d", answer);
    printf("\n");

    return 0;
}