#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int n, m;
    std::cin >> n >> m;
    
    std::vector<int> a_lst(n);
    for(int i = 0; i < n; ++i)
        std::cin >> a_lst[i];
    
    std::vector<int> b_lst(m);
    for(int i = 0; i < m; ++i)
        std::cin >> b_lst[i];

    std::vector<int> cand;

    // Sort in ascending order
    std::sort(a_lst.begin(), a_lst.end());
    std::sort(b_lst.begin(), b_lst.end());

    auto [min_a, max_b] = std::minmax_element(a_lst.begin(), a_lst.end(), b_lst.begin(), b_lst.end());

    if (*min_a > *max_b) {
        cand.push_back(*max_b + 1);
    }
    else {
        for (int i = n-1; i >= 0; --i) {
            int x_a = a_lst[i];
            auto it = std::lower_bound(b_lst.begin(), b_lst.end(), x_a);

            if (n - i >= m - (it - b_lst.begin())) {
                cand.push_back(x_a);
            }
        }
    }

    std::cout << *std::min_element(cand.begin(), cand.end());
    
    return 0;
}
