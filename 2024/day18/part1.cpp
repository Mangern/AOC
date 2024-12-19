#include <array>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

constexpr int N = 71;
constexpr int M = 71;
constexpr int K = 1024;

int grid[N * M];
vector<array<int, 2>> coords;

int main() {
    for (int i = 0; i < N * M; ++i) {
        grid[i] = numeric_limits<int>::max();
    }
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

    for (int i = 0; i < K; ++i) {
        auto [x, y] = coords[i];
        grid[y * M + x] = -1;
    }
    
    queue<int> q;
    grid[0] = 0;
    q.push(0);

    while (q.size()) {
        int u = q.front();
        q.pop();

        int i = u / M;
        int j = u % M;

        for (auto [ni, nj] : vector<array<int,2>>{{i - 1, j}, {i + 1, j}, {i, j - 1}, {i, j + 1}}) {
            if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;

            int v = ni * M + nj;

            if (grid[v] > grid[u] + 1) {
                grid[v] = grid[u] + 1;
                q.push(v);
            }
        }
    }
    cout << grid[N * M - 1] << endl;
}
