#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ii = pair<ll,ll>;

void p1() {
    ll a, b;
    cin >> a >> b;

    --a, --b;

    bool turn = true;

    ll num_rolls = 0;

    ll next_roll = 1;

    ll a_score = 0;
    ll b_score = 0;

    while (a_score < 1000 && b_score < 1000) {
        ll roll = 0;

        roll += next_roll;

        next_roll += 1;
        if (next_roll > 100)next_roll = 1;
        roll += next_roll;

        next_roll += 1;
        if (next_roll > 100)next_roll = 1;
        roll += next_roll;

        num_rolls += 3;
        next_roll += 1;
        if (next_roll > 100)next_roll = 1;

        if (turn) {
            a = (a + roll) % 10;

            a_score += a + 1;
        } else {
            b = (b + roll) % 10;

            b_score += b + 1;
        }
        turn = !turn;
    }

    ll ans = num_rolls * min(a_score, b_score);

    cout << ans << endl;
}

ll dp[22][22][22][10][10]; // turn, p1 score, p2 score, p1 pos, p2 pos

void p2() {
    ll a_start, b_start;
    cin >> a_start >> b_start;
    --a_start, --b_start;

    vector<ii> outcomes = {{3,1}, {4,3}, {5,6}, {6,7}, {7,6}, {8,3}, {9,1}};

    memset(dp, 0, sizeof dp);

    dp[0][0][0][a_start][b_start] = 1;

    ll ans1 = 0;
    ll ans2 = 0;

    for (int turn = 0; turn < 21; ++turn) {
        for (ll p1_score = 0; p1_score < 21; ++p1_score) {
            for (ll p2_score = 0; p2_score < 21; ++p2_score) {
                for (ll p1_pos = 0; p1_pos < 10; ++p1_pos) {
                    for (ll p2_pos = 0; p2_pos < 10; ++p2_pos) {
                        for (auto pp1 : outcomes) {
                            for (auto pp2 : outcomes) {
                                ll res1 = pp1.first;
                                ll num1 = pp1.second;
                                ll res2 = pp2.first;
                                ll num2 = pp2.second;

                                ll land1 = (p1_pos + res1) % 10;
                                ll land2 = (p2_pos + res2) % 10;

                                ll np1_score = min(21LL, p1_score + land1 + 1);
                                ll np2_score = min(21LL, p2_score + land2 + 1);

                                dp[turn+1][np1_score][np2_score][land1][land2] += num1*num2*dp[turn][p1_score][p2_score][p1_pos][p2_pos];

                            }
                        }
                    }
                }
            }
        }
    }

    for (int turn = 0; turn < 22; ++turn) {
        for (ll p1_pos = 0; p1_pos < 10; ++p1_pos) {
            for (ll p2_pos = 0; p2_pos < 10; ++p2_pos) {
                for (ll p2_score = 0; p2_score < 22; ++p2_score) {
                    ans1 += dp[turn][21][p2_score][p1_pos][p2_pos];
                }

                for (ll p1_score = 0; p1_score < 21; ++p1_score) {
                    ans2 += dp[turn][p1_score][21][p1_pos][p2_pos];
                }
            }
        }
    }

    cout << max(ans1, ans2) << endl;
}

int main() {
    p2();
    return 0;
}
