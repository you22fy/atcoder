#include <iostream>
#include <vector>

using namespace std;

class FenwickTree
{
private:
    vector<int> tree;
    int n;

    int func(int a, int b)
    {
        return a ^ b;
    }

public:
    FenwickTree(int size) : n(size), tree(size + 1, 0) {}

    void update(int idx, int value)
    {
        for (; idx <= n; idx += idx & -idx)
            tree[idx] = func(tree[idx], value);
    }

    int query(int idx)
    {
        int result = 0;
        for (; idx > 0; idx -= idx & -idx)
            result = func(result, tree[idx]);
        return result;
    }

    int range_query(int l, int r)
    {
        return query(r) ^ query(l - 1);
    }
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    vector<int> A(N);
    for (int i = 0; i < N; ++i)
    {
        cin >> A[i];
    }

    FenwickTree ft(N);
    vector<int> xor_cumsum(N + 1, 0);
    for (int i = 0; i < N; ++i)
    {
        xor_cumsum[i + 1] = xor_cumsum[i] ^ A[i];
        ft.update(i + 1, A[i]);
    }

    long long ans = 0;
    for (int i = 1; i < N - 1; ++i)
    {
        for (int j = i + 1; j < N; ++j)
        {
            int xor_range = ft.range_query(i + 1, j + 1);
            ans += xor_range;
        }
    }

    cout << ans << endl;

    return 0;
}
