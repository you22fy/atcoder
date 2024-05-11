#include <iostream>
#include <vector>
using namespace std;

int main()
{
    const int MOD = 100000000;

    int n;
    cin >> n;

    vector<int> a(n);
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }

    long long sumA = 0;  // a[i]の累積和
    long long res = 0;   // 最終的な結果

    for (int j = 0; j < n; j++)
    {
        // a[j]をj回足す（前の全てのa[i]とペアになるため）
        res = (res + a[j] * j) % MOD;
        // 今までのa[i]の和を加える
        sumA = (sumA + a[j]) % MOD;
    }

    // 全体の合計にMODを適用
    res = (res + sumA) % MOD;

    cout << res << endl;

    return 0;
}
