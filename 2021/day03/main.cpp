#include <bits/stdc++.h>
using namespace std;

const int WSIZE = 12;
    
int cnt[WSIZE];


int main() {
    string line;



    while (getline(cin, line)) {
        reverse(begin(line), end(line));

        for (int i = 0; i < WSIZE; ++i) {
            if (line[i] == '1')++cnt[i];
            else --cnt[i];
        }
    }

    int a = 0, b = 0;

    // 2^12 * 2^12 = 2^24 < 2^32
    //

    for (int i = 0; i < WSIZE; ++i) {
        if (cnt[i] > 0)a |= (1<<i);
        else b |= (1<<i);
    }
    cout << a << " " << b << endl;

    cout << a*b << endl;



    return 0;
}
