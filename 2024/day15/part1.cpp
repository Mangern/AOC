#include <cassert>
#include <cstdio>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<string> grid;
    string line;

    for (;;) {
        getline(cin, line);
        if (line.empty()) break;
        grid.push_back(line);
    }

    string prog;

    while (getline(cin, line)) {
        prog.append(line);
    }

    int n = grid.size();
    int m = grid[0].size();

    int ri, rj;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '@') {
                ri = i;
                rj = j;
            }
        }
    }

    function<bool(int,int,int,int)> mov = [&] (int i, int j, int di, int dj) {
        int ni = i + di;
        int nj = j + dj;

        if (grid[ni][nj] == '#') return false;

        if (grid[ni][nj] != '.') {
            if (!mov(ni, nj, di, dj)) return false;
        }

        grid[ni][nj] = grid[i][j];
        grid[i][j] = '.';
        return true;
    };

    for (char c : prog) {
        int di, dj;
        switch (c) {
            case '<':
                di = 0;
                dj = -1;
                break;
            case '>':
                di = 0;
                dj = 1;
                break;
            case '^':
                di = -1;
                dj = 0;
                break;
            case 'v':
                di = 1;
                dj = 0;
                break;
            default:
                assert(false);
        }

        if (mov(ri, rj, di, dj)) {
            ri += di;
            rj += dj;
        }

        assert(grid[ri][rj] == '@');
    }

    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'O') {
                ans += 100 * i + j;
            }
        }
    }
    cout << ans << endl;
}
