#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
template<typename t, size_t N>
using ar = array<t,N>;
using ii = ar<ll,2>;
using vii = vector<ii>;
using ld = long double;

#define all(v) begin(v), end(v)

const int INF = numeric_limits<int>::max();
const ll INFLL = numeric_limits<ll>::max();

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
ll myRand(ll B) {
	return (unsigned ll)rng() % B;
}
template<typename t>
istream& operator >> (istream& in, vector<t>& vec) {
    for (t& x : vec)in >> x;
    return in;
}

template<typename t>
ostream& operator << (ostream& out, vector<t>& vec) {
    int n = (int)vec.size();
    for (int i = 0; i < n; ++i) {
        out << vec[i];
        if (i < n - 1)out << " ";
    }
    return out;
}

// t should support min-function (operator <)
template<typename t>
t min(const vector<t>& vec) {
    t ans = vec[0];
    for (const auto& el : vec) {
        ans = min(ans, el);
    }
    return ans;
}

// t should support max-function (operator <)
template<typename t>
t max(const vector<t>& vec) {
    t ans = vec[0];
    for (const auto& el : vec) {
        ans = max(ans, el);
    }
    return ans;
}
const int mxN = 3e4+3;

void testCase() {
    int n;
    cin >> n;

    vector<char> op(n);
    vector<ll> opn(n);
    vll test(n);
    vector<vll> items(n, vll());
    vector<vi> adj(n, vi(2));

    ll md = 1;
    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        items[i] = vll(k);
        cin >> items[i];
        cin >> op[i];
        string s;
        cin >> s;
        if (s == "old") {
            op[i] = 's';
        } else opn[i] = stoll(s);
        cin >> test[i];
        cin >> adj[i][1];
        cin >> adj[i][0];

        md *= test[i];
    }
    cout << md << endl;

    vll ans(n, 0);

    for (int r = 0; r < 10000; ++r) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < items[i].size(); ++j) {
                ll x = items[i][j];
                if (op[i] == 's') {
                    x *= x;
                } else if (op[i] == '*') {
                    x *= opn[i];
                } else x += opn[i];

                x %= md;
                bool b = (x % test[i] == 0);
                items[adj[i][b]].push_back(x);
            }
            ans[i] += items[i].size();
            items[i].clear();
        }
    }

    sort(all(ans));
    reverse(all(ans));
    cout << ans[0] * ans[1] << endl;
}

void setIO() {
    cin.tie(0)->sync_with_stdio(0);
}

void pre() {

}

int main() {
    setIO();
    pre();
    int t = 1;

    for (int tc = 1; tc <= t; ++tc) {
        testCase();
    }
    return 0;
}
