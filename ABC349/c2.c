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
    char s_upper[MAX_S_LENGTH];

    for (int i = 0; i < len_s; i++)
    {
        s_upper[i] = toupper(s[i]);
    }

    if (t[2] == 'X')
    {
        // 2文字
        for (int i = 0; i < len_s; i++)
        {
            if (s_upper[i] == t[0])
            {
                for (int j = i + 1; j < len_s; j++)
                {
                    if (s_upper[j] == t[1])
                    {
                        printf("Yes\n");
                        return 0;
                    }
                }
            }
        }
    }
    else
    {
        // 3文字
        for (int i = 0; i < len_s; i++)
        {
            if (s_upper[i] == t[0])
            {
                for (int j = i + 1; j < len_s; j++)
                {
                    if (s_upper[j] == t[1])
                    {
                        for (int k = j + 1; k < len_s; k++)
                        {
                            if (s_upper[k] == t[2])
                            {
                                printf("Yes\n");
                                return 0;
                            }
                        }
                    }
                }
            }
        }
    }

    printf("No\n");
    return 0;
}
