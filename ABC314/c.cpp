#include <iostream>
#include <vector>
#include <string>

int main() {
    int n, m;
    std::cin >> n >> m;

    std::string s;
    std::cin >> s;

    std::vector<int> c(n);
    for(int i = 0; i < n; ++i) {
        std::cin >> c[i];
    }

    for(int i = 1; i <= m; ++i) {
        std::vector<int> p;

        // Collect positions of characters to be rotated
        for(int j = 0; j < n; ++j) {
            if(c[j] == i) {
                p.push_back(j);
            }
        }

        if (!p.empty()) {
            // Rotate by swapping characters
            char last_char = s[p.back()];
            for(int k = p.size() - 1; k > 0; --k) {
                s[p[k]] = s[p[k-1]];
            }
            s[p[0]] = last_char;
        }
    }

    std::cout << s << std::endl;
    return 0;
}
