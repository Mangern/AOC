#include <algorithm>
#include <iostream>
#include <string>
#include <map>
#include <vector>

using namespace std;

map<string, int> id;
vector<string> rid;
int n;
vector<vector<int>> adj;

int main() {
    string line;
    while (getline(cin, line)) {
        string us = line.substr(0, 2);
        string vs = line.substr(3, 2);
        if (!id.count(us)) {
            rid.push_back(us);
            id[us] = n++;
        }

        if (!id.count(vs)) {
            rid.push_back(vs);
            id[vs] = n++;
        }

        int u = id[us];
        int v = id[vs];

        while (adj.size() < n)adj.push_back(vector<int>());
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int ans = 0;
    for (int u = 0; u < n; ++u) {
        for (int v : adj[u]) if (v > u) {
            for (int w : adj[v]) if (w > v) {
                if (rid[u][0] != 't' && rid[v][0] != 't' && rid[w][0] != 't') continue;
                if (find(begin(adj[w]), end(adj[w]), u) != end(adj[w]))
                    ++ans;
            }
        }
    }
    cout << ans << endl;
}
