#include <algorithm>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

int n;
vector<string> as;

bool dfs(const string_view& target, int i) {
    if (i == target.length()) return true;
    else if (i > target.length()) return false;

    string_view rem = target.substr(i, target.length());

    for (int j = 0; j < n; ++j) {
        if (rem.substr(0, as[j].length()) == as[j]) {
            if (dfs(target, i + as[j].length())) return true;
        }
    }
    return false;
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

    string_view sv;
    int ans = 0;
    while (getline(cin, line)) {
        sv = line;
        if (dfs(sv, 0)) {
            ++ans;
        }
    }
    cout << ans << endl;
}
