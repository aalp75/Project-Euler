
#include <bits/stdc++.h>

#ifdef LOG
#include "debug.h"
#else
#define debug(...)
#endif

using namespace std;
typedef long long ll;

ll LIM;

vector<ll> prime_divisor;

// precompute all the prime divisors from 1 to LIM using the sieve of eratosthenes
void precompute_prime_divisors() {
    prime_divisor.resize(LIM + 1, -1);
    vector<bool> is_prime(LIM + 1, true);
    for (int i = 2; i <= LIM; i++) {
        if (!is_prime[i]) continue;
        prime_divisor[i] = i;
        for (int j = 2 * i; j <= LIM; j += i) {
            is_prime[j] = false;
            if (prime_divisor[j] == -1) {
                prime_divisor[j] = i;
            }
        }
    }   
}

ll perimeter(ll& c1, ll& c2, ll& c3) {
    return c1 + c2 + c3;
}

// return the prime decomposition of a number x = p1 ^ q1 + p2 ^ q2 + ... + p2 ^ qn
// in the form {{p1, q1}, {p2, q2}, ..., {pn, qn}}
vector<pair<ll, ll>> compute_prime_decomposition(ll x) {
    
    map<int, int> prime_decomposition_map;
    while (prime_divisor[x] > 1) {
        prime_decomposition_map[prime_divisor[x]]++;
        x /= prime_divisor[x];
    }
    vector<pair<ll, ll>> prime_decomposition;
    for (auto keyval : prime_decomposition_map) {
        prime_decomposition.push_back({keyval.first, keyval.second});
    }
    return prime_decomposition;
}

// merge 2 prime decompositions vector
vector<pair<ll, ll>> merge(vector<pair<ll, ll>>& p1, vector<pair<ll, ll>>& p2) {
    vector<pair<ll, ll>> p;
    int n1 = p1.size(); int n2 = p2.size();
    int ite1 = 0;
    int ite2 = 0;
    while (ite1 < n1 || ite2 < n2) {
        if (ite1 == n1) {
            p.push_back(p2[ite2]);
            ite2++;
            continue;
        }
        else if (ite2 == n2) {
            p.push_back(p1[ite1]);
            ite1++;
            continue;
        }
        else if (p1[ite1].first == p2[ite2].first) {
            p.push_back({p1[ite1].first, p1[ite1].second + p2[ite2].second});
            ite1++; ite2++;
            continue;
        }
        else if (p1[ite1].first < p2[ite2].first) {
            p.push_back(p1[ite1]);
            ite1++;
            continue;
        }
        else {
            p.push_back(p2[ite2]);
            ite2++;
        }

    }
    return p;
}

vector<ll> generate_all_divisors(vector<pair<ll, ll>>& prime_decomposition) {
    vector<ll> divisors = {1};

    int n = prime_decomposition.size();

    for (int i = 0; i < n; i++) {
        int m = divisors.size();
        vector<ll> additional_divisors;
        ll prime = prime_decomposition[i].first;
        ll val = prime;
        for (int power = 0; power < prime_decomposition[i].second; power++) {
            for (int j = 0; j < m; j++) {
                additional_divisors.push_back(divisors[j] * val);
            }
            val *= prime;
        }

        for (auto e : additional_divisors) {
            divisors.push_back(e);
        }
    }
    return divisors;
}; 

void solve() {

    ll ans = (LIM - 1) / 2; // all solution of the form (1, x, x)

    // loop on a and used the factorized form: (a - 1) * (a + 1) = (c - b) * (c + b)
    // compute the prime decomposition of (a - 1) and (a + 1)
    // compute all the divisors of (a - 1) * (a + 1)
    // find all the divisors matching the condition for b & c
    // i.e. a <= b <= c and a + b + c <= LIM
    for (ll a = 2; a <= LIM / 3; a++) {

        auto p1 = compute_prime_decomposition(a - 1);
        auto p2 = compute_prime_decomposition(a + 1);
        auto p = merge(p1, p2);

        auto factors = generate_all_divisors(p);

        ll prod = (a -1) * (a + 1);

        for (ll factor : factors) {
            ll other_factor = prod / factor;
 
            if ((factor + other_factor) % 2 != 0 || factor > other_factor) continue;
            
            ll c = (other_factor + factor) / 2;
            ll b = (other_factor - factor) / 2;

            if (perimeter(a, b, c) <= LIM && a <= b && b <= c) {
                ans += 1;
            }
        }
    }
    cout << "Solution: " << ans << endl;
}

int main() {
    LIM = 25e6;
    precompute_prime_divisors();
    solve();
    return 0;
}