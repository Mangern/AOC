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
    string line;
    vector<string> grid;
    while(getline(cin,line)) {
        grid.push_back(line);
    }

    int n = grid.size();
    int m = grid[0].size();

    auto cti = [&] (int i, int j) {
        return i * m + j;
    };

    auto get_el = [&] (int i, int j) {
        if (grid[i][j] == 'S')return 'a';
        if (grid[i][j] == 'E')return 'z';
        return grid[i][j];
    };

    vector<vi> adj(n*m, vi());

    int s,e;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            for (auto [ni,nj] : vector<ii>{{i-1,j},{i+1,j},{i,j+1},{i,j-1}}) {
                if (ni < 0 || ni >= n || nj < 0 || nj >= m)continue;

                char curr_el = get_el(i,j);
                char neig_el = get_el(ni,nj);

                if (neig_el <= curr_el + 1) {
                    adj[cti(i,j)].push_back(cti(ni,nj));
                }
                if (grid[i][j] == 'S')s = cti(i,j);
                if (grid[i][j] == 'E')e = cti(i,j);
            }
        }
    }

    queue<int> q;
    vi dist(n*m, -1);

    q.push(s);
    dist[s] = 0;

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : adj[u])if (dist[v] == -1) {
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    cout << dist[e] << endl;
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
