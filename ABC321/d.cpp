#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m, p;
    long int answer = 0;
    int tmp;
    cin >> n >> m >> p;
    vector<int> a(n);
    vector<int> b(m);
    for (int i = 0; i < n; i++)
    {
        cin >> tmp;
        a[i] = tmp;
    }
    for (int i = 0; i < m; i++)
    {
        cin >> tmp;
        b[i] = tmp;
    }
    for(int i = 0; i < n ; i ++){
        for(int j = 0; j < m ; j++){
            answer += min(a[i] + b[j], p);
        }
    }
    cout << answer  << endl;
}