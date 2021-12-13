#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using ii = pair<int,int>;

int sign(int x) {
    if (x < 0) {
        return -1;
    } else if (x > 0) {
        return 1;
    } else {
        return 0;
    }
}

void p1() {
    int n;
    cin >> n;

    map<ii, int> cnt;

    for (int i = 0; i < n; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        int dx = sign(c - a);
        int dy = sign(d - b);

        if (!(dx == 0 || dy == 0))continue;

        do {
            cnt[{a,b}]++;
            a += dx;
            b += dy;
        } while (a != c || b != d);
        cnt[{a,b}]++;
    }

    int ans = 0;
    for (auto pp : cnt) {
        if (pp.second > 1) {
            ++ans;
        }
    }

    cout << ans << endl;
}

void p2() {
    int n;
    cin >> n;

    map<ii, int> cnt;

    for (int i = 0; i < n; ++i) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;

        int dx = sign(c - a);
        int dy = sign(d - b);


        do {
            cnt[{a,b}]++;
            a += dx;
            b += dy;
        } while (a != c || b != d);
        cnt[{a,b}]++;
    }

    int ans = 0;
    for (auto pp : cnt) {
        if (pp.second > 1) {
            ++ans;
        }
    }

    cout << ans << endl;
}

int main() {
    //p1();
    p2();
    return 0;
}
