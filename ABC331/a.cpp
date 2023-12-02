#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

void solve()
{
    int M, D;
    int y, m, d;
    cin >> M >> D >> y >> m >> d;
    if (d == D) //月末
    {
        if (m == M) // 年末
        {
            cout << y + 1 << " " << 1 << " " << 1 << endl;
        }
        else
        {
            cout << y << " " << m+1 << " " << 1 << endl;
        }
    }
    else
    {
        cout << y  << " " << m << " " << d+1 << endl;
    }
}

int main()
{
    solve();
    return 0;
}
