#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <map>

using namespace std;
using ll = long long;

int n;
vector<string> as;

map<string, ll> dp;

ll dfs(const string& target, int i) {
    if (i == target.length()) return 1;
    else if (i > target.length()) return 0;


    string rem = target.substr(i, target.length());

    if (dp.count(rem)) return dp[rem];

    ll ret = 0;
    for (int j = 0; j < n; ++j) {
        if (rem.substr(0, as[j].length()) == as[j]) {
            ret += dfs(target, i + as[j].length());
        }
    }
    return dp[rem] = ret;
}

int main() {
    string line;
    getline(cin, line);
    istringstream iss(line);
    string tok;
    while(getline(iss, tok, ',')) {
        tok.erase(tok.begin(), find_if(tok.begin(), tok.end(), [](unsigned char ch) {
            return !isspace(ch);
        }));
        as.push_back(tok);
    }
    n = as.size();
    sort(begin(as), end(as));

    getline(cin, line);

    ll ans = 0;
    while (getline(cin, line)) {
        ans += dfs(line, 0);
    }
    cout << ans << endl;
}
