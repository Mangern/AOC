#include <array>
#include <cstdio>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>
using namespace std;

using tup = array<int, 5>;

tup convert_lock(const vector<string>& grid) {
    tup lock;
    for (int j = 0; j < 5; ++j) {
        int i;
        for (i = 1; i < 7; ++i) {
            if (grid[i][j] == '.') break;
        }
        lock[j] = i - 1;
    }
    return lock;
}

tup convert_key(const vector<string>& grid) {
    tup key;
    for (int j = 0; j < 5; ++j) {
        int i;
        for (i = 6; i > 0; --i) {
            if (grid[i][j] == '.') break;
        }
        key[j] = 5 - i;
    }
    return key;
}

ostream& operator<<(ostream& os, const tup& t) {
    for (int i = 0; i < 5; ++i) {
        os << t[i];
        if (i < 4)os << ' ';
    }
    return os;
}

int main() {
    string line;
    vector<tup> locks;
    vector<tup> keys;
    while (getline(cin, line)) {
        vector<string> grid;
        grid.push_back(line);
        for (int i = 0; i < 6; ++i) {
            getline(cin, line);
            grid.push_back(line);
        }
        getline(cin, line);

        if (grid[0][0] == '#')locks.push_back(convert_lock(grid));
        else keys.push_back(convert_key(grid));
    }

    int ans = 0;
    for (const auto& lk : locks) for (const auto& ky : keys) {
        bool good = 1;
        for (int i = 0; i < 5; ++i) {
            if (lk[i] + ky[i] >= 6) {
                good = 0;
                break;
            }
        }
        ans += good;
    }
    cout << ans << endl;
}
