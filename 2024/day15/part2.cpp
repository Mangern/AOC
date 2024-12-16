#include <cassert>
#include <cstdio>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<string> grid;
    string line;

    for (;;) {
        getline(cin, line);
        if (line.empty()) break;
        string row;
        for (char c : line) {
            switch (c) {
                case '#':
                    row.push_back('#');
                    row.push_back('#');
                    break;
                case 'O':
                    row.push_back('[');
                    row.push_back(']');
                    break;
                case '.':
                    row.push_back('.');
                    row.push_back('.');
                    break;
                case '@':
                    row.push_back('@');
                    row.push_back('.');
                    break;
            }
        }
        grid.push_back(row);
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

    function<void(int, int, int, int, set<int>&)> collect = [&] (int i, int j, int di, int dj, set<int>& idxs) {
        if (grid[i][j] == '.' || grid[i][j] == '#') return;
        if (idxs.count(i * m + j)) return;
        int ni = i + di;
        int nj = j + dj;

        idxs.insert(i * m + j);

        collect(ni, nj, di, dj, idxs);

        if (grid[i][j] == '[') {
            collect(i, j + 1, di, dj, idxs);
        }
        if (grid[i][j] == ']') {
            collect(i, j - 1, di, dj, idxs);
        }
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

        set<int> tomove;
        collect(ri, rj, di, dj, tomove);

        bool canmove = 1;
        for (int idx : tomove) {
            int i = idx / m;
            int j = idx % m;

            if (grid[i + di][j + dj] == '#') {
                canmove = 0;
                break;
            }
        }
        if (canmove) {
            vector<string> ngrid(n, string(m, '.'));

            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    if (!tomove.count(i * m + j)) {
                        ngrid[i][j] = grid[i][j];
                    }
                }
            }

            for (int idx : tomove) {
                ngrid[idx / m + di][idx % m + dj] = grid[idx / m][idx % m];
            }

            ri += di;
            rj += dj;

            grid = ngrid;
        }
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '[') {
                ans += 100 * i + j;
            }
        }
    }
    cout << ans << endl;
}
