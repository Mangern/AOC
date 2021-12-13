#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;

#define INFLL (numeric_limits<ll>::max())


void p1() {
    int n;
    cin >> n;


    vll buck(9, 0);
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;

        ++buck[x];
    }

    for (int d = 1; d <= 80; ++d) {
        vll nbuck(9, 0);
        for (int i = 0; i < 9; ++i) {
            if (i == 0) {
                nbuck[6] += buck[i];
                nbuck[8] += buck[i];
            } else {
                nbuck[i-1] += buck[i];
            }
        }
        buck = nbuck;
    }

    ll ans = 0;

    for (auto x : buck) {
        assert(INFLL - x >= ans);
        ans += x;
    }

    cout << ans << endl;

}

void p2() {
    int n;
    cin >> n;


    vll buck(9, 0);
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;

        ++buck[x];
    }

    for (int d = 1; d <= 256; ++d) {
        vll nbuck(9, 0);
        for (int i = 0; i < 9; ++i) {
            if (i == 0) {
                nbuck[6] += buck[i];
                nbuck[8] += buck[i];
            } else {
                nbuck[i-1] += buck[i];
            }
        }
        buck = nbuck;
    }

    ll ans = 0;

    for (auto x : buck) {
        assert(INFLL - x >= ans);
        ans += x;
    }

    cout << ans << endl;

}

int main() {
    //p1();
    p2();
    return 0;
}
