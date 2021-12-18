#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const int SZ = 5;

struct Board {
    set<int> rows[SZ];
    set<int> cols[SZ];

    ll sum = 0;
    bool won = false;

    Board() {
    }

    void init(vector<vector<int>> grid) {
        for (int i = 0; i < SZ; ++i) {
            for (int j = 0; j < SZ; ++j) {
                rows[i].insert(grid[i][j]);
                cols[j].insert(grid[i][j]);
                sum += grid[i][j];
            }
        }

        assert(rows[0].size() == 5);
    }

    bool cross(int x) {
        bool f = 0;
        for (int i = 0; i < SZ; ++i) {
            if (rows[i].count(x)) {
                sum -= x;
            }
            rows[i].erase(x);
            cols[i].erase(x);

            if (rows[i].empty() || cols[i].empty()) {
                f = 1;
            }
        }
        if (f) {
            if (won) {
                return false;
            } else {
                won = true;
                return true;
            }
        }
        return false;
    }
};


istream& operator >> (istream& in, Board& board) {
    vector<vector<int>> grid(SZ, vector<int>(SZ, 0));
    for (int i = 0; i < SZ; ++i) {
        for (int j = 0; j < SZ; ++j) {
            in >> grid[i][j];
        }
    }
    board.init(grid);
    return in;
}

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    for (auto& x : nums)cin >> x;

    vector<Board> boards(n);

    for (int i = 0; i < n; ++i) {
        cin >> boards[i];

    }

    ll ans;

    for (int i = 0; i < n; ++i) {
        ll curr = nums[i];

        for (int j = 0; j < n; ++j) {
            if (boards[j].cross(curr)) {
                ans = boards[j].sum * curr;
            }
        }
    }
    cout << ans << endl;
    return 0;
}
