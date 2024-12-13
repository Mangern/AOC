#include <iostream>
#include <map>
#include <numeric>
#include <vector>
#include <array>

using namespace std;

struct UnionFind {
    vector<int> p;

    UnionFind(int n) {
        p.resize(n);
        iota(begin(p), end(p), 0);
    }

    int find(int i) {
        if (p[i] == i) return i;
        return p[i] = find(p[i]);
    }

    bool join(int i, int j) {
        i = find(i);
        j = find(j);
        if (i == j) return false;
        p[i] = j;
        return true;
    }
};

int main() {
    string line;
    vector<string> grid;
    int n, m;
    while (getline(cin, line)) {
        grid.push_back(line);
    }
    n = grid.size();
    m = grid[0].size();

    UnionFind uf(n * m);

    for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
        if (i > 0 && grid[i-1][j] == grid[i][j]) {
            uf.join(i * m + j, (i - 1) * m + j);
        }

        if (j > 0 && grid[i][j - 1] == grid[i][j]) {
            uf.join(i * m + j, i * m + j - 1);
        }
    }

    map<int, vector<int>> groups;

    for (int i = 0; i < n * m; ++i) {
        groups[uf.find(i)].push_back(i);
    }

    vector<array<bool, 4>> vis(n * m, array<bool,4>{0,0,0,0});

    int ans = 0;
    for (auto& [k, v] : groups) {
        int area = v.size();
        int per = 0;
        for (int idx : v) {
            int i = idx / m;
            int j = idx % m;

            bool top = (i == 0 || grid[i-1][j] != grid[i][j]);
            bool bot = (i == n - 1 || grid[i+1][j] != grid[i][j]);
            bool rgt = (j == m - 1 || grid[i][j+1] != grid[i][j]);
            bool lft = (j == 0 || grid[i][j-1] != grid[i][j]);

            if (top && !vis[idx][0]) {
                ++per;
                for (int k = 0; ; ++k) {
                    if (j + k >= m || grid[i][j+k] != grid[i][j]) break;
                    if (i != 0 && grid[i-1][j+k] == grid[i][j]) break;
                    vis[i * m + j + k][0] = 1;
                }
            }

            if (bot && !vis[idx][1]) {
                ++per;
                for (int k = 0; ; ++k) {
                    if (j + k >= m || grid[i][j+k] != grid[i][j])break;
                    if (i != n - 1 && grid[i+1][j+k] == grid[i][j]) break;

                    vis[i * m + j + k][1] = 1;
                }
            }

            if (rgt && !vis[idx][2]) {
                ++per;
                for (int k = 0; ; ++k) {
                    if (i + k >= n || grid[i+k][j] != grid[i][j]) break;
                    if (j != m - 1 && grid[i+k][j+1] == grid[i][j]) break;
                    vis[(i + k) * m + j][2] = 1;
                }
            }
            if (lft && !vis[idx][3]) {
                ++per;
                for (int k = 0;; ++k) {
                    if (i + k >= n || grid[i+k][j] != grid[i][j]) break;
                    if (j != 0 && grid[i+k][j-1] == grid[i][j]) break;
                    vis[(i + k) * m + j][3] = 1;
                }
            }
        }
        ans += per * area;
    }
    cout << ans << endl;
}
