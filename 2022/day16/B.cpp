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
const ll K = 26;
using mp_t = unordered_map<ll,ll>;

ll n, m;
vll flow;
vector<vll> dist;
vll has_pos;

vector<vector<vector<vector<mp_t>>>> dp;
ll calc(ll u1, ll u2, ll t1, ll t2, ll mask) {
    if (min(t1,t2) >= K)return 0;
    t1 = min(t1,K);
    t2 = min(t2,K);
    if (u1 > u2) {
        swap(u1,u2);
        swap(t1,t2);
    }

    if (dp[u1][u2][t1][t2].count(mask))return dp[u1][u2][t1][t2][mask];

    ll ret = 0;
    for (ll i = 0; i < m; ++i) {
        if (mask & (1LL<<i))continue;
        for (ll j = 0; j < m; ++j) if (j != i) {
            if (mask & (1LL<<j))continue;
            ll there1 = t1 + dist[u1][has_pos[i]] + 1;
            ll there2 = t2 + dist[u2][has_pos[j]] + 1;

            ll c = flow[has_pos[i]] * max(0LL, K - there1) + flow[has_pos[j]] * max(0LL, K - there2);
            c += calc(has_pos[i], has_pos[j], there1, there2, mask | (1LL<<i) | (1LL << j));
            ret = max(ret,c);
        }
    }
    dp[u1][u2][t1][t2][mask] = ret;
    return ret;
}

void testCase() {
    cin >> n;
    ll start;
    cin >> start;

    flow = vll(n);
    cin >> flow;

    for (ll i = 0; i < n; ++i)if (flow[i])has_pos.push_back(i);
    m = has_pos.size();

    dist = vector<vll>(n,vll(n, 0));

    for (int i = 0; i < n * n; ++i) {
        ll u,v,d;
        cin >> u >> v >> d;
        dist[u][v] = d;
        dist[v][u] = d;
    }

    dp = vector<vector<vector<vector<mp_t>>>>(n,vector<vector<vector<mp_t>>>(n,vector<vector<mp_t>>(K+1,vector<mp_t>(K+1, mp_t()))));
    cout << calc(start, start, 0, 0, 0) << endl;
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
    //cin >> t;

    for (int tc = 1; tc <= t; ++tc) {
        testCase();
    }
    return 0;
}
