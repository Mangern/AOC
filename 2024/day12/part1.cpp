#include <iostream>
#include <map>
#include <numeric>
#include <vector>

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

    int ans = 0;
    for (auto& [k, v] : groups) {
        int area = v.size();
        int per = 0;
        for (int idx : v) {
            int i = idx / m;
            int j = idx % m;

            for (auto [ni, nj] : vector<pair<int,int>>{{i-1,j},{i+1,j},{i,j-1},{i,j+1}}) {
                if (ni < 0 || ni >= n || nj < 0 || nj >= m) {
                    ++per;
                    continue;
                }

                per += (grid[ni][nj] != grid[i][j]);
            }
        }
        ans += per * area;
    }
    cout << ans << endl;
}
