#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;
using ll = long long;

vector<int> prog = {2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0};

bool compat(string& bits, int j, int val) {
    if (bits[j] != 'x' && (bits[j]-'0') != (val&1))return false;
    if (bits[j+1] != 'x' && (bits[j+1]-'0') != ((val>>1)&1))return false;
    if (bits[j+2] != 'x' && (bits[j+2]-'0') != ((val>>2)&1))return false;
    return true;
}

ll mini = numeric_limits<ll>::max();

void dfs(int i, int j, string bits) {
    if (i >= prog.size()) {
        //cout << bits << endl;
        reverse(begin(bits), end(bits));
        for (int k = 0; k < bits.length(); ++k) {
            if (bits[k] == 'x')bits[k] = '0';
        }
        ll res = stoll(bits, nullptr, 2);
        if (res < mini) {
            cout << "New best: " << res << endl;
            mini = res;
        }
        //exit(0);
        return;
    }
    // goal of this it: bruteforce bits[j:j+3]
    while (bits.length() < j+3) {
        bits.push_back('x');
    }

    for (int val = 0; val < 8; ++val) {
        if (!compat(bits, j, val)) continue;
        string nbits = bits;
        int c = prog[i] ^ 0b011 ^ val;
        int wj = j + (val ^ 0b101);
        while (nbits.length() < wj + 3)nbits.push_back('x');
        nbits[j] = '0'+(val&1);
        nbits[j+1] = '0'+((val>>1)&1);
        nbits[j+2] = '0'+((val>>2)&1);
        if (!compat(nbits, wj, c)) continue;
        nbits[wj] = '0'+(c&1);
        nbits[wj+1] = '0'+((c>>1)&1);
        nbits[wj+2] = '0'+((c>>2)&1);
        dfs(i + 1, j + 3, nbits);
    }
}

int main() {
    dfs(0, 0, string());
}
