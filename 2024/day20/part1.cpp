#include <iostream>
#include <limits>
#include <map>
#include <queue>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

int n, m;
int s, t;

vector<int> adj(int u) {
    int i = u / m;
    int j = u % m;

    vector<int> ret;
    for (auto [ni, nj] : vector<pair<int,int>>{{i-1,j},{i+1,j},{i,j-1},{i,j+1}}) {
        if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
        ret.push_back(ni * m + nj);
    }
    return ret;
}

vector<ll> race(const string& grid) {
    vector<ll> dist(n * m, numeric_limits<ll>::max());
    dist[s] = 0;
    queue<int> q;
    q.push(s);
    while (q.size()) {
        int u = q.front();
        q.pop();

        for (int v : adj(u)) {
            if (grid[v] == '#') continue;
            if (dist[u] + 1 >= dist[v]) continue;
            dist[v] = dist[u] + 1;
            q.push(v);
        }
    }
    return dist;
}

int main() {
    string grid;
    string line;
    while (getline(cin, line)) {
        grid.append(line);
        m = line.length();
        ++n;
    }

    for (int i = 0; i < n*m; ++i) {
        if (grid[i] == 'S')s = i;
        if (grid[i] == 'E')t = i;
    }

    auto dists = race(grid);
    ll base = dists[t];

    ll ans = 0;
    for (int u = 0; u < n * m; ++u) {
        if (grid[u] != '#') continue;
        int enter = u;
        for (int v : adj(u)) {
            if (dists[v] < dists[enter]) {
                enter = v;
            }
        }

        for (int v : adj(u)) {
            if (grid[v] == '#') continue;
            if (dists[enter] + 2 < dists[v]) {
                ll save = dists[v] - dists[enter] - 2;
                if (save >= 100)++ans;
            }
        }

    }

    cout << ans << endl;

    return 0;
}
