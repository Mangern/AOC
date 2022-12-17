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
const ll mxN = 4000001;

void testCase() {
    int n;
    cin >> n;

    vector<vii> segs(mxN, vii());

    for (int i = 0; i < n; ++i) {
        ll x1,y1,x2,y2;
        cin >> x1 >> y1 >> x2 >> y2;


        ll d = abs(x1-x2)+abs(y1-y2);

        ll l = x1, r = x1;
        ll stay = max(y1-d,0LL);

        for (ll y = y1 - d; y <= y1; ++y) {
            r = max(r,0LL);
            l = min(l,mxN-1);
            if (y > 0 && y < mxN)segs[y].push_back({max(0LL,l),min(r,mxN-1)});
            --l;
            ++r;
        }

        l = x1;
        r = x1;
        for (ll y = y1 + d; y > y1; --y) {
            r = max(r,0LL);
            l = min(l,mxN-1);
            if (y > 0 && y < mxN)segs[y].push_back({max(0LL,l),min(r,mxN-1)});
            --l;
            ++r;
        }
    }

    ll ax = -1 , ay = - 1;
    for (int i = 0; i < mxN; ++i) {
        sort(all(segs[i]));

        ll far = -1;
        for (auto [l,r] : segs[i]) {
            if (l - far > 1) {
                ax = l - 1;
                ay = i;
                break;
            }
            far = max(far,r);
        }
    }
    ax *= 4000000;
    ax += ay;
    cout << ax << endl;
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
