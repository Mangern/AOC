#include <array>
#include <iostream>
#include <limits>
#include <queue>
#include <string>
#include <vector>

using namespace std;
using ll = long long;
using ii = array<ll,2>;

int n, m;
int s, t;

void adj(int u, vector<int>& ret) {
    ret.clear();
    if (u % m > 0)ret.push_back(u - 1);
    if (u % m < m - 1)ret.push_back(u + 1);
    if (u >= m)ret.push_back(u - m);
    if (u + m < n * m)ret.push_back(u + m);
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

    vector<ll> dists(n * m, numeric_limits<ll>::max());
    dists[s] = 0;
    queue<int> q;
    q.push(s);
    vector<int> vadj;
    while (q.size()) {
        int u = q.front();
        q.pop();

        adj(u, vadj);
        for (int v : vadj) {
            if (grid[v] == '#') continue;
            if (dists[u] + 1 >= dists[v]) continue;
            dists[v] = dists[u] + 1;
            q.push(v);
        }
    }

    ll ans = 0;
    for (int ui = 0; ui < n; ++ui) {
        for (int uj = 0; uj < m; ++uj) {
            int u = ui * m + uj;
            if (grid[u] == '#') continue;
            for (int vi = max(0, ui - 21); vi < min(n, ui + 21); ++vi) {
                for (int vj = max(0, uj - 21); vj < min(m, uj + 21); ++vj) {
                    int v = vi * m + vj;
                    if (grid[v] == '#') continue;

                    ll cheat = abs(ui - vi) + abs(uj - vj);

                    if (cheat > 20) {
                        continue;
                    }
                    ll save = dists[v] - (dists[u] + cheat);
                    if (save >= 100)++ans;
                }
            }
        }
    }

    cout << ans << endl;

    return 0;
}

