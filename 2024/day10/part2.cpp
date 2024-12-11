#include <iostream>
#include <string>
#include <vector>
#include <array>

using namespace std;
using ll = long long;
using vll = vector<ll>;
using ii = array<int,2>;

int n, m;
vector<vll> dp;
vector<string> grid;

ll score(int i, int j) {
    ll& ret = dp[i][j];
    if (ret != -1) return ret;

    if (grid[i][j] == '9') return ret = 1;

    ret = 0;
    for (auto [ni, nj] : vector<ii>{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
        if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
        
        if (grid[ni][nj] == grid[i][j] + 1) {
            ret += score(ni, nj);
        }
    }

    return ret;
}

int main() {

    string line;
    while (getline(cin, line)) {
        grid.push_back(line);
    }

    n = grid.size();
    m = grid[0].size();

    dp = vector<vll>(n, vll(m, -1));

    ll ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '0') {
                ll s = score(i, j);
                ans += s;
            }
        }
    }
    cout << ans << endl;
}
