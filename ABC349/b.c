#include <stdio.h>
#include <string.h>

#define TRUE 1
#define FALSE 0

int main()
{
    char s[101];
    int count[26] = {0};
    int frequency_count[101] = {0};
    int max_frequency = 0;

    scanf("%s", s);

    for (int i = 0; s[i] != '\0'; i++)
    {
        count[s[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++)
    {
        if (count[i] > 0)
        {
            frequency_count[count[i]]++;
            if (count[i] > max_frequency)
            {
                max_frequency = count[i];
            }
        }
    }

    int is_good_string = TRUE;
    for (int i = 1; i <= max_frequency; i++)
    {
        if (frequency_count[i] != 0 && frequency_count[i] != 2)
        {
            is_good_string = 0;
            break;
        }
    }

    if (is_good_string)
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }

    return 0;
}
