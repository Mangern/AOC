#include <bits/stdc++.h>
using namespace std;

const int WSIZE = 12;
    
int oxy(vector<int> v, int idx = WSIZE - 1) {
    cout << idx << endl;
    cout << v.size() << endl;
    if (v.size() == 1)return v[0];

    int cnt = 0;

    for (int x : v) {
        if (x & (1 << idx))++cnt;
        else --cnt;
    }

    vector<int> nvec;

    for (int x : v) {
        int bt = (x & (1 << idx)) >> idx;

        if (cnt > 0) {
            if (bt == 1)nvec.push_back(x);
        } else if (cnt < 0) {
            if (bt == 0)nvec.push_back(x);
        } else {
            if (bt == 1)nvec.push_back(x);
        }
    }

    return oxy(nvec, idx - 1);
}

int co2(vector<int> v, int idx = 11) {
    if (v.size() == 1)return v[0];

    int cnt = 0;

    for (int x : v) {
        if (x & (1 << idx))++cnt;
        else --cnt;
    }

    vector<int> nvec;

    for (int x : v) {
        int bt = (x & (1 << idx)) >> idx;

        if (cnt > 0) {
            if (bt == 0)nvec.push_back(x);
        } else if (cnt < 0) {
            if (bt == 1)nvec.push_back(x);
        } else {
            if (bt == 0)nvec.push_back(x);
        }
    }

    return co2(nvec, idx - 1);
}

int main() {
    string line;


    vector<int> nums;

    while (getline(cin, line)) {
        nums.push_back(stoi(line, 0, 2));
    }

    int a = oxy(nums);

    int b = co2(nums);

    cout << a * b << endl;

    return 0;
}
