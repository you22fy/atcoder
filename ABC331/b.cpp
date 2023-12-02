#include <iostream>
#include <string>
#include <map>
#include <set>
#include <vector>
#include<algorithm>
#include <climits>
using namespace std;

void solve() {
    int n, s, m, l;
    cin >> n >> s >> m >> l;

    int maxEggs = n + 12;

    vector<int> dp(maxEggs, INT_MAX);

    dp[0] = 0;

    for (int i = 0; i <= n; i++) {
        if (dp[i] != INT_MAX) {
            if (i + 6 < maxEggs) dp[i + 6] = min(dp[i + 6], dp[i] + s);
            if (i + 8 < maxEggs) dp[i + 8] = min(dp[i + 8], dp[i] + m);
            if (i + 12 < maxEggs) dp[i + 12] = min(dp[i + 12], dp[i] + l);
        }
    }

    int answer = *min_element(dp.begin() + n, dp.end());

    cout << answer << endl;
}

int main()
{
    solve();
    return 0;
}
