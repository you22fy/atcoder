// なぜかTLE

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_S_LENGTH 100001

int main()
{
    char s[MAX_S_LENGTH];
    char t[4];
    scanf("%s", s);
    scanf("%s", t);

    int len_s = strlen(s);

    for (int i = 0; i < len_s; i++)
    {
        for (int j = i + 1; j < len_s; j++)
        {
            if (toupper(s[i]) == t[0] && toupper(s[j]) == t[1] && 'X' == t[2])
            {
                printf("Yes\n");
                return 0;
            }

            for (int k = j + 1; k < len_s; k++)
            {
                if (toupper(s[i]) == t[0] && toupper(s[j]) == t[1] && toupper(s[k]) == t[2])
                {
                    printf("Yes\n");
                    return 0;
                }
            }
        }
    }

    printf("No\n");
    return 0;
}
