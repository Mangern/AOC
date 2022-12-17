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

    int N;
    cin >> N;

    vector<vi> grid(N, vi(N,0));
    int out_color = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            char c;
            cin >> c;
            grid[i][j] = (c == '#');
        }
    }

    auto apply = [&](const vector<vi> grid) {
        int n = grid.size();
        vector<vi> res(n+2, vi(n+2, out_color));

        for (int i = -1; i < n + 1; ++i) {
            for (int j = -1; j < n + 1; ++j) {
                int t_idx = 0;
                for (int di = -1; di <= 1; ++di) {
                    t_idx <<= 3;
                    for (int dj = -1; dj <= 1; ++dj) {
                        int r = i+di;
                        int c = j+dj;

                        int bit = (r >= 0 && r < n && c >= 0 && c < n) ? grid[r][c] : out_color;

                        t_idx |= (bit << (1 - dj));
                    }
                }

                res[i+1][j+1] = table[t_idx];
            }
        }

        if (out_color) {
            out_color = table[511];
        } else {
            out_color = table[0];
        }

        return res;
    };


    auto print_grid = [&] () {
        for (auto row : grid) {
            for (auto x : row) {
                cout << x;
            }
            cout << endl;
        }
        cout << endl;
    };

    grid = apply(grid);
    grid = apply(grid);

    int ans = 0;

    for (auto row : grid)
        for (int x : row)
            ans += x;
    cout << ans << endl;
}

void p2() {
    bitset<512> table;

    for (int i = 0; i < 512; ++i) {
        char c;
        cin >> c;

        table[i] = (c == '#');
    }

    int N;
    cin >> N;

    vector<vi> grid(N, vi(N,0));
    int out_color = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            char c;
            cin >> c;
            grid[i][j] = (c == '#');
        }
    }

    auto apply = [&](const vector<vi> grid) {
        int n = grid.size();
        vector<vi> res(n+2, vi(n+2, out_color));

        for (int i = -1; i < n + 1; ++i) {
            for (int j = -1; j < n + 1; ++j) {
                int t_idx = 0;
                for (int di = -1; di <= 1; ++di) {
                    t_idx <<= 3;
                    for (int dj = -1; dj <= 1; ++dj) {
                        int r = i+di;
                        int c = j+dj;

                        int bit = (r >= 0 && r < n && c >= 0 && c < n) ? grid[r][c] : out_color;

                        t_idx |= (bit << (1 - dj));
                    }
                }

                res[i+1][j+1] = table[t_idx];
            }
        }

        if (out_color) {
            out_color = table[511];
        } else {
            out_color = table[0];
        }

        return res;
    };


    auto print_grid = [&] () {
        for (auto row : grid) {
            for (auto x : row) {
                cout << x;
            }
            cout << endl;
        }
        cout << endl;
    };

    for (int i = 0; i < 50; ++i) {
        grid = apply(grid);
    }

    long long ans = 0;

    for (auto row : grid)
        for (int x : row)
            ans += x;
    cout << ans << endl;
}

int main() {
    p2();
    return 0;
}
