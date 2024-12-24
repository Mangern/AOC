#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <map>
#include <vector>

using namespace std;

map<string, int> id;
vector<string> rid;
int n;
vector<vector<int>> adj;
vector<vector<int>> mat;

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
    mat.assign(n, vector<int>(n, 0));
    for (int u = 0; u < n; ++u) for (int v : adj[u]) {
        mat[u][v] = 1;
    }
    vector<vector<int>> cliqs;

    for (int u = 0; u < n; ++u) for (int v : adj[u]) if (v > u) {
        vector<int> c;
        c.push_back(u);
        c.push_back(v);
        cliqs.push_back(c);
    }

    for (;;) {
        cout << "Size: " << cliqs[0].size() << " (" << cliqs.size() << " cliques total)" << endl;
        vector<vector<int>> ncliqs;

        for (const auto& cliq : cliqs) {
            for (int v = cliq.back() + 1; v < n; ++v) {
                bool good = 1;
                for (int w : cliq) if (!mat[w][v]) {
                    good = 0;
                    break;
                }

                if (good) {
                    vector<int> ncliq = cliq;
                    ncliq.push_back(v);

                    ncliqs.push_back(ncliq);
                }
            }
        }

        if (ncliqs.empty()) break;
        cliqs = ncliqs;
    }

    vector<string> fin;
    for (int u : cliqs[0]) {
        fin.push_back(rid[u]);
    }
    sort(begin(fin), end(fin));
    cout << fin[0];

    for (int i = 1; i < fin.size(); ++i) {
        cout << "," << fin[i];
    }
    cout << endl;
}
