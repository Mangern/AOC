#include <bits/stdc++.h>
using namespace std;

using vi = vector<int>;
using ii = pair<int,int>;


void p1() {
    bitset<512> table;

    for (int i = 0; i < 512; ++i) {
        char c;
        cin >> c;

        table[i] = (c == '#');
    }

    int n;
    cin >> n;

    vector<vi> grid(n, vi(n,0));
    int out_color = 0;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            char c;
            cin >> c;
            grid[i][j] = (c == '#');
        }
    }

    auto apply = [=](const vector<vi> grid) {
        vector<vi> res(n+2, vi(n+2, out_color));

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                int t_idx = 0;
                for (int r = -1; r <= 1; ++r) {
                    t_idx <<= 3;
                    for (int c = -1; c <= 1; ++c) {
                        int curr = (i+r >= 0 && i + r < n && j + c >= 0 && j + c < n) ? grid[i+r][j+c] : out_color;

                        t_idx |= (1 << (c - 1));
                    }
                }
                res[i+1][j+1] = table[t_idx];
            }
        }

        for (int i = 0; i < n + 2; ++i) {
            vector<ii> positions = {{0,i}, {i,0}, {n-1, i}, {i,n-1}};
            for (auto pos : positions) {

            }
        }
        return res;
    };

    grid = apply(grid);
    grid = apply(grid);

    int ans = 0;

    for (auto row : grid)
        for (int x : row)
            ans += x;
    cout << ans << endl;
}

int main() {
    p1();
    return 0;
}
