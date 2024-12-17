#include <array>
#include <functional>
#include <iostream>
#include <limits>
#include <queue>
#include <set>
#include <vector>

using namespace std;
using ll = long long;

using ii = array<ll, 2>;

// NESW
int n, m;
vector<string> grid;

int coord(int i, int j, int dir) {
    return dir * n * m + i * m + j;
}

int main() {
    string line;
    while (getline(cin, line)) {
        grid.push_back(line);
    }

    n = grid.size();
    m = grid[0].size();

    vector<vector<ii>> adj(4 * n * m, vector<ii>());

    vector<ll> dist(4 * n * m, numeric_limits<ll>::max());
    vector<vector<int>> cf(4 * n * m, vector<int>());

    int s;
    int ei, ej;


    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '#') continue;
            if (grid[i][j] == 'S') {
                s = coord(i, j, 1);
            }
            if (grid[i][j] == 'E') {
                ei = i;
                ej = j;
            }

            if (grid[i-1][j] != '#') 
                adj[coord(i, j, 0)].push_back({coord(i - 1, j, 0), 1});

            if (grid[i][j+1] != '#')
                adj[coord(i, j, 1)].push_back({coord(i, j + 1, 1), 1});

            if (grid[i+1][j] != '#')
                adj[coord(i, j, 2)].push_back({coord(i + 1, j, 2), 1});

            if (grid[i][j-1] != '#')
                adj[coord(i, j, 3)].push_back({coord(i, j - 1, 3), 1});

            for (int dir = 0; dir < 4; ++dir) {
                adj[coord(i, j, dir)].push_back({coord(i, j, (dir+1)%4), 1000});
                adj[coord(i, j, dir)].push_back({coord(i, j, (dir+3)%4), 1000});
            }
        }
    }

    dist[s] = 0;
    priority_queue<ii, vector<ii>, greater<ii>> pq;
    pq.push({0, s});

    while (pq.size()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (dist[u] < d) continue;

        for (auto [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
                cf[v].clear();
                cf[v].push_back(u);
            } else if (dist[u] + w == dist[v]) {
                cf[v].push_back(u);
            }
        }
    }

    ll ans = numeric_limits<ll>::max();
    int e;
    for (int dir = 0; dir < 4; ++dir) {
        int u = coord(ei, ej, dir);
        if (dist[u] < ans) {
            ans = dist[u];
            e = u;
        }
    }

    queue<int> q;
    set<int> vis;
    q.push(e);
    vis.insert(e);
    set<int> uniq;
    int cnt = 0;
    while (q.size()) {
        int u = q.front();
        q.pop();
        int i = (u % (n * m)) / m;
        int j = (u % (n * m)) % m;
        grid[i][j] = 'O';
        uniq.insert(i * m + j);

        for (int v : cf[u]) {
            if (!vis.count(v)) {
                vis.insert(v);
                q.push(v);
            }
        }
    }
    cout << uniq.size() << endl;
}
