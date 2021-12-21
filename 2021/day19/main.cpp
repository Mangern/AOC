#pragma GCC optimize("Ofast", "unroll-loops")
#include <bits/stdc++.h>
using namespace std;
using ll = long long;

using i3 = array<ll,3>;
using m3 = array<array<int,3>, 3>;


const i3 ORIGIN = {0,0,0};

struct i3_hash {
    inline std::size_t operator()(const i3& p) const {
        return (p[0]+1000) * 100000 + (p[1] + 1000)*1000 + (p[0]+1000);
    }
};

i3 apply(m3 mat, i3 vec) {
    i3 res = {0,0,0};

    for (int r = 0; r < 3; ++r) {
        for (int c = 0; c < 3; ++c) {
            res[r] += mat[r][c] * vec[c];
        }
    }
    return res;
}


int ROTATIONS[24][3][3] = {
    {
        { 1, 0, 0},
        { 0, 1, 0},
        { 0, 0, 1}
    },
    {
        { 0, 0, 1},
        { 0, 1, 0},
        {-1, 0, 0}
    },
    {
        {-1, 0, 0},
        { 0, 1, 0},
        { 0, 0,-1}
    },
    {
        { 0, 0,-1},
        { 0, 1, 0},
        { 1, 0, 0}
    },
    {
        { 0,-1, 0},
        { 1, 0, 0},
        { 0, 0, 1}
    },
    {
        { 0, 0, 1},
        { 1, 0, 0},
        { 0, 1, 0}
    },
    {
        { 0, 1, 0},
        { 1, 0, 0},
        { 0, 0,-1}
    },
    {
        { 0, 0,-1},
        { 1, 0, 0},
        { 0,-1, 0}
    },
    {
        { 0, 1, 0},
        {-1, 0, 0},
        { 0, 0, 1}
    },
    {
        { 0, 0, 1},
        {-1, 0, 0},
        { 0,-1, 0}
    },
    {
        { 0,-1, 0},
        {-1, 0, 0},
        { 0, 0,-1}
    },
    {
        { 0, 0,-1},
        {-1, 0, 0},
        { 0, 1, 0}
    },
    {
        { 1, 0, 0},
        { 0, 0,-1},
        { 0, 1, 0}
    },
    {
        { 0, 1, 0},
        { 0, 0,-1},
        {-1, 0, 0}
    },
    {
        {-1, 0, 0},
        { 0, 0,-1},
        { 0,-1, 0}
    },
    {
        { 0,-1, 0},
        { 0, 0,-1},
        { 1, 0, 0}
    },
    {
        { 1, 0, 0},
        { 0,-1, 0},
        { 0, 0,-1}
    },
    {
        { 0, 0,-1},
        { 0,-1, 0},
        {-1, 0, 0}
    },
    {
        {-1, 0, 0},
        { 0,-1, 0},
        { 0, 0, 1}
    },
    {
        { 0, 0, 1},
        { 0,-1, 0},
        { 1, 0, 0}
    },
    {
        { 1, 0, 0},
        { 0, 0, 1},
        { 0,-1, 0}
    },
    {
        { 0,-1, 0},
        { 0, 0, 1},
        {-1, 0, 0}
    },
    {
        {-1, 0, 0},
        { 0, 0, 1},
        { 0, 1, 0}
    },
    {
        { 0, 1, 0},
        { 0, 0, 1},
        { 1, 0, 0}
    }
};

m3 to_mat(int r_idx) {
    m3 res;

    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            res[i][j] = ROTATIONS[r_idx][i][j];
        }
    }
    return res;
}

struct Scanner {
    int id;
    size_t n_points;
    vector<i3> points;

    vector<vector<i3>> orientations;

    Scanner() {}

    void init(const vector<i3> _points) {
        for (auto p : _points)points.push_back(p);
        n_points = points.size();

    }

    bool operator<(const Scanner& other) const {
        return id < other.id;
    }

    vector<vector<i3>> get_orientations() {
        if (orientations.size())return orientations;
        vector<vector<i3>> res;
        for (int k = 0; k < 24; ++k) {
            // apply ROTATIONS[k]
            m3 rot = to_mat(k);
            vector<i3> row;
            for (i3 p : points) {
                row.push_back(apply(rot, p));
            }
            res.push_back(row);
        }
        return orientations = res;
    }
};

istream& operator>>(istream& in, Scanner& s) {
    int k;
    in >> k;

    vector<i3> ps(k);

    for (i3& p : ps) {
        in >> p[0] >> p[1] >> p[2];
    }

    s.init(ps);

    return in;
}

i3 operator-(const i3 lft, const i3 rgt) {
    return {lft[0] - rgt[0], lft[1] - rgt[1], lft[2] - rgt[2]};
}

i3 operator+(const i3 lft, const i3 rgt) {
    return {lft[0] + rgt[0], lft[1] + rgt[1], lft[2] + rgt[2]};
}

void p1() {
    int n;
    cin >> n;

    vector<Scanner> scanners(n);
    for (int i = 0; i < n; ++i) {
        cin >> scanners[i];
        scanners[i].id = i;
    }

    unordered_set<i3, i3_hash> global_set;
    for (auto p : scanners[0].points) {
        global_set.insert(p);
    }

    vector<bool> vis(n, false);
    vis[0] = true;

    int num_vis = 1;

    while (num_vis < n) {
        for (int i = 0; i < n; ++i) {
            if (vis[i])continue;

            // check if scanners[i] has >= 12 points in common with
            // global_set (account for translation)
            const vector<vector<i3>> point_orientations = scanners[i].get_orientations();

            bool found = 0;

            for (int ori_idx = 0; ori_idx < 24; ++ori_idx) {
                auto point_test = point_orientations[ori_idx];
                // now we have a set of points
                // we want to find out if at least 12 of these points correspond with 
                // some points in the global set
                // such that they are all shifted by the same vector
                // this vector could be any 
                for (auto p : point_test) {
                    for (auto ref_p : global_set) {
                        i3 diff = ref_p - p;

                        // shift all points in point test by this diff vector
                        // check if they are in global_set
                        int match = 0;

                        for (auto x : point_test) {
                            if (global_set.count(x + diff))++match;
                        }

                        if (match >= 12) {
                            found = 1;
                            for (auto x : point_test) {
                                global_set.insert(x+diff);
                            }
                            break;
                        }
                    }
                    if (found)break;
                }
                if (found)break;
            }

            if (found) {
                num_vis += 1;
                vis[i] = 1;
            }
        }
    }

    cout << global_set.size() << endl;
}

void p2() {
    int n;
    cin >> n;

    vector<Scanner> scanners(n);
    for (int i = 0; i < n; ++i) {
        cin >> scanners[i];
        scanners[i].id = i;
    }

    unordered_set<i3, i3_hash> global_set;
    for (auto p : scanners[0].points) {
        global_set.insert(p);
    }

    vector<bool> vis(n, false);
    vis[0] = true;

    int num_vis = 1;

    vector<i3> scanner_pos(n, {0,0,0});

    scanner_pos[0] = {0,0,0};
    

    while (num_vis < n) {
        for (int i = 0; i < n; ++i) {
            if (vis[i])continue;

            // check if scanners[i] has >= 12 points in common with
            // global_set (account for translation)
            const vector<vector<i3>> point_orientations = scanners[i].get_orientations();

            bool found = 0;

            for (int ori_idx = 0; ori_idx < 24; ++ori_idx) {
                const auto point_test = point_orientations[ori_idx];
                // now we have a set of points
                // we want to find out if at least 12 of these points correspond with 
                // some points in the global set
                // such that they are all shifted by the same vector
                // this vector could be any 
                for (auto p : point_test) {
                    for (auto ref_p : global_set) {
                        i3 diff = ref_p - p;

                        // shift all points in point test by this diff vector
                        // check if they are in global_set
                        int match = 0;

                        for (auto x : point_test) {
                            if (global_set.count(x + diff))++match;
                        }


                        if (match >= 12) {
                            // for p2: calculate scanner position
                            // its actually just the shift
                            scanner_pos[i] = diff;
                            found = 1;
                            for (auto x : point_test) {
                                global_set.insert(x+diff);
                            }
                            break;
                        }
                    }
                    if (found)break;
                }
                if (found)break;
            }

            if (found) {
                num_vis += 1;
                vis[i] = 1;
            }
        }
    }

    ll ans = 0;

    for (auto p : scanner_pos) {
        for (auto q : scanner_pos) {
            ans = max(ans, abs(p[0] - q[0]) + abs(p[1] - q[1]) + abs(p[2] - q[2]));
        }
    }
    cout << ans << endl;
}

int main() {
    p2();
    return 0;
}
