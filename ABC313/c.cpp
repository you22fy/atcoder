#include <iostream>
#include <vector>
#include <algorithm>

int main(){
    int n;
    std::cin >> n;
    std::vector<int> a(n);
    for(int i = 0; i< n; i++){
        std::cin >> a[i];
    }
    std::sort(a.begin(), a.end());
    int c = 0;

    while (true) {
        if (a[n - 1] - a[0] < 1) {
            break;
        } else {
            a[n - 1] -= 1;
            a[0] += 1;
            if (a[n - 1] < a[n - 2]) {
                std::swap(a[n - 1], a[n - 2]);
            }
            if (a[0] > a[1]) {
                std::swap(a[0], a[1]);
            }
            c += 1;
        }
    }
    std::cout << c << std::endl;

    return 0;
}
