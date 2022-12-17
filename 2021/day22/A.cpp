#include <bits/stdc++.h>
using namespace std;
template<typename t, size_t n>
using ar = array<t,n>;
using ii = ar<int,2>;
using tup = ar<ii,3>;
const int mxN = 101;

pair<bool, tup> parse(string s) {
    bool on = s.find(' ') == 2;
    tup res;

    int i = s.find('=')+1;
    int j = s.find('.');

    res[0][0] = stoi(s.substr(i, j-i));
    i = j+2;
    j = s.find(',',i);

    res[0][1] = stoi(s.substr(i,j-i));

    i = s.find('=',i)+1;
    j = s.find('.',i);
    res[1][0] = stoi(s.substr(i,j-i));
    i=j+2;
    j = s.find(',',i);
    res[1][1] = stoi(s.substr(i,j-i));

    i = s.find('=',i)+1;
    j = s.find('.',i);

    res[2][0] = stoi(s.substr(i,j-i));
    i = j+2;
    j = s.size();

    res[2][1] = stoi(s.substr(i,j));
    return {on,res};
}

bool grid[mxN][mxN][mxN];

int main() {
    string line;
    vector<pair<bool,tup>> a;
    while (getline(cin, line)) {
        a.push_back(parse(line));
    }

    vector<pair<bool,tup>> b;
    for (auto& pp : a) {
        tup& t = pp.second;

        bool bd = 0;
        for (int i= 0; i < 3; ++i) {
            if (t[i][0] > 50 || t[i][1] < -50)bd = 1;

            t[i][0] = max(t[i][0], -50);
            t[i][1] = min(t[i][1], 50);
        }
        if (!bd)b.push_back(pp);
    }
    for (auto pp : b) {
        auto t = pp.second;

        for (int i = t[0][0]; i <= t[0][1]; ++i) {
            for (int j = t[1][0]; j <= t[1][1]; ++j) {
                for (int k = t[2][0]; k <= t[2][1]; ++k) {
                    if (pp.first)grid[50+i][50+j][50+k] = 1;
                    else grid[50+i][50+j][50+k] = 0;
                }
            }
        }
    }

    int ans = 0;
    for (int i = 0; i < mxN; ++i)for (int j = 0; j < mxN; ++j)for (int k = 0; k < mxN; ++k)if (grid[i][j][k])++ans;
    cout << ans << endl;
}
