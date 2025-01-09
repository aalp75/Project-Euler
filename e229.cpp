
#include <bits/stdc++.h>
#include <chrono>

#ifdef LOG
#include "debug.h"
#else
#define debug(...)
#endif

using namespace std;

typedef long long ll;

ll LIM;

ll solve() {

    map<int, int> multiplier = {{1, 1}, {2, 2}, {3, 4}, {7, 8}};

    ll bound = ceil(sqrt(LIM));

    vector<short> v(LIM + 10, 0);

    for (auto keyval : multiplier) {
        for (ll x = 1; x <= bound; x++) {
            for (ll y = 1; y <= bound; y++) {
                ll n = x * x + keyval.first * y * y;
                if (n <= LIM) {
                    v[n] |= keyval.second;
                }
                else {
                    break;
                }
            }
        }
    }

    ll ans = 0;
    for (auto e : v) {
        if (e == 15) {
            ans++;
        }
    }
    return ans;
}

int main() {
    LIM = 2e9;
    auto start = clock();
    auto ans = solve();
    float duration = float(clock() - start) / CLOCKS_PER_SEC;
    cout << "Solution: " << ans << " (time elapsed: " << duration << " seconds)" << endl;
}