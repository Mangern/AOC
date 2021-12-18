// ugly ass code
#include <bits/stdc++.h>
using namespace std;
using vi = vector<int>;
using ll = long long;

#define all(v) begin(v), end(v)

int n, m, k;
vector<vi> adj;
set<int> lowers;
int s_node, e_node;

bool is_small(int x) {
    return lowers.count(x);
}

// a,b in small
// only go through big
ll num_ways(vector<bool>& vis,int a, int b) {
    if (a == b) {
        ll res = 0;
        for (int i : adj[a]) {
            if (!is_small(i))++res;
        }
        return res;
    }
    if (vis[a])return 0;
    vis[a] = 1;
    ll sum = 0;
    for (int i : adj[a]) {
        if (i == b) {
            sum += 1;
            continue;
        }

        if (is_small(i)) continue;

        sum += num_ways(vis, i, b);
    }
    return sum;
}

ll solve1(set<int>& small, int s, int e) {
    if (s == e)return 1;

    vector<int> in_small;
    for (auto x : small)in_small.push_back(x);

    ll from_this = 0;

    for (auto x : in_small) {
        // find ways from s to x
        vector<bool> vis(n, false);
        ll w = num_ways(vis, s, x);

        //cout << "from " << s << " to " << x << ": " << w << endl;

        if (!w)continue;

        small.erase(x);
        from_this += w * solve1(small, x, e);
        small.insert(x);
    }
    //cout << "Total from " << s << " to " << e << ": " << from_this << endl;
    return from_this;
} 

void p1() {
    cin >> n >> m >> k;
    int s,e;
    cin >> s >> e;

    s_node = s;
    e_node = e;

    set<int> small;
    adj.assign(n, vi());
    for (int i = 0; i < k; ++i) {
        int a;
        cin >> a;
        lowers.insert(a);
        small.insert(a);
    }
    small.insert(e);
    lowers.insert(s);
    lowers.insert(e);

    for (int i = 0; i < m; ++i) {
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    ll ans = solve1(small, s, e);


    cout << ans << endl;
}

ll solve2(vi mid_path) {
    sort(all(mid_path));
    ll ans = 0;
    do {
        vi path;
        path.push_back(s_node);
        for (auto x : mid_path)path.push_back(x);
        path.push_back(e_node);
        ll comb = 1;

        for (int i = 1; i < path.size(); ++i) {
            // number of paths from i-1 to i
            
            set<int> lft, rgt;

            int a = path[i-1];
            int b = path[i];

            for (int x : adj[a])lft.insert(x);
            for (int x : adj[b])rgt.insert(x);

            ll sum = 0;

            if (a == b) {
                for (auto x : lft) {
                    if (!is_small(x))++sum;
                }
            } else {
                if (lft.count(b))++sum;
                for (auto x : lft) {
                    if (!is_small(x) && rgt.count(x))++sum;
                }
            }
            comb *= sum;
        }
        ans += comb;

    } while(next_permutation(all(mid_path)));
    return ans;
}

void p2() {
    cin >> n >> m >> k;
    int s,e;
    cin >> s >> e;
    s_node = s;
    e_node = e;

    set<int> small;
    adj.assign(n, vi());

    vector<int> poss;

    for (int i = 0; i < k; ++i) {
        int a;
        cin >> a;
        lowers.insert(a);
        poss.push_back(a);
    }
    lowers.insert(s);
    lowers.insert(e);
    for (int i = 0; i < m; ++i) {
        int a,b;
        cin >> a >> b;
        adj[a].push_back(b);
    }

    ll ans = 0;
    for (int mask = 0; mask < (1<<k); ++mask) {
        vector<int> mid_path;
        for (int i = 0; i < k; ++i) {
            if (mask & (1<<i))mid_path.push_back(poss[i]);
        }

        for (auto x : mid_path) {
            vector<int> nmid_path = mid_path;
            nmid_path.push_back(x);

            ans += solve2(nmid_path);
        }
        ans += solve2(mid_path);
    }


    cout << ans << endl;
    
}

int main() {
    p1();
    //p2();
    return 0;
}
