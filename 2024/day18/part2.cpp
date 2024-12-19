#include <array>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct UnionFind {
    int num_sets;
    vector<int> p, sz, rnk;
    UnionFind(int n) {
        num_sets = n;
        p = vector<int>(n);
        iota(begin(p), end(p),0);
        rnk = vector<int>(n,0);
        sz = vector<int>(n,1);
    }

    int find(int i) {
        if (p[i] == i)return i;
        return p[i] = find(p[i]);
    }

    bool check(int i, int j) {
        return find(i)==find(j);
    }

    bool join(int i, int j) {
        i = find(i);
        j = find(j);
        if (i == j)return 0;
        if (rnk[i] < rnk[j]) {
            sz[j] += sz[i];
            p[i] = j;
        } else {
            sz[i] += sz[j];
            p[j] = i;
            if (rnk[i] == rnk[j]) {
                ++rnk[i];
            }
        }
        --num_sets;
        return 1;
    }
};

constexpr int N = 71;
constexpr int M = 71;

int grid[N * M];
vector<array<int, 2>> coords;

int main() {
    string line;
    while(getline(cin, line)) {
        istringstream iss(line);
        string coord;
        getline(iss, coord, ',');
        int x = stoi(coord);
        getline(iss, coord, ',');
        int y = stoi(coord);
        coords.push_back({x, y});
    }

    for (auto [x, y] : coords) {
        ++grid[y * M + x];
    }

    UnionFind uf(N * M);

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            if (grid[i * M + j] != 0) continue;
            if (i > 0 && grid[(i - 1) * M + j] == 0) {
                uf.join(i * M + j, (i - 1) * M + j);
            }
            if (j > 0 && grid[i * M + j - 1] == 0) {
                uf.join(i * M + j, i * M + j - 1);
            }
        }
    }

    for (int k = coords.size() - 1; k >= 0; --k) {
        auto [j, i] = coords[k];

        int u = i * M + j;

        if (!--grid[u]) {
            for (auto [ni, nj] : vector<array<int,2>>{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
                if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
                if (grid[ni * M + nj] != 0) continue;

                int v = ni * M + nj;
                uf.join(u, v);
            }
        }

        if (uf.check(0, N * M - 1)) {
            cout << j << "," << i << endl;
            break;
        }
    }
}
