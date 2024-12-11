#include <bitset>
#include <iostream>
#include <string>
#include <vector>
#include <array>

using namespace std;

constexpr int K = 3000;


using ll = long long;
using vll = vector<ll>;
using ii = array<int,2>;
using mask_t = bitset<K>;

int n, m;

vector<vector<mask_t>> dp;
vector<vector<bool>> calc;
vector<string> grid;


mask_t& score(int i, int j) {
    if (calc[i][j]) return dp[i][j];

    calc[i][j] = 1;

    if (grid[i][j] == '9') {
        dp[i][j].set(i * m + j);
        return dp[i][j];
    }

    auto& ret = dp[i][j];
    for (auto [ni, nj] : vector<ii>{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
        if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
        
        if (grid[ni][nj] == grid[i][j] + 1) {
            ret |= score(ni, nj);
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

    dp = vector<vector<mask_t>>(n, vector<mask_t>(m));
    calc = vector<vector<bool>>(n, vector<bool>(m, 0));

    ll ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '0') {
                auto s = score(i, j);
                ans += s.count();
            }
        }
    }
    cout << ans << endl;
}
