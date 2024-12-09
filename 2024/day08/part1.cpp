#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main() {
    vector<string> grid;
    string line;

    while (getline(cin, line)) {
        grid.push_back(line);
    }

    int n = grid.size();
    int m = grid[0].size();

    map<char, vector<pair<int, int>>> antennas;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '.') continue;
            antennas[grid[i][j]].push_back({i,j});
        }
    }

    set<pair<int,int>> anti;

    for (const auto& [type, locations] : antennas) {
        for (int i = 0; i < locations.size(); ++i)
            for (int j = i + 1; j < locations.size(); ++j) {
                auto [y1, x1] = locations[i];
                auto [y2, x2] = locations[j];

                int dy = y2 - y1;
                int dx = x2 - x1;

                int anti_y1 = y1 + 2 * dy;
                int anti_x1 = x1 + 2 * dx;

                if (0 <= anti_y1 && anti_y1 < n && 0 <= anti_x1 && anti_x1 < m)
                    anti.insert({anti_y1, anti_x1});

                
                int anti_y2 = y2 - 2 * dy;
                int anti_x2 = x2 - 2 * dx;

                if (0 <= anti_y2 && anti_y2 < n && 0 <= anti_x2 && anti_x2 < m)
                    anti.insert({anti_y2, anti_x2});

            }
    }

    cout << anti.size() << endl;
}
