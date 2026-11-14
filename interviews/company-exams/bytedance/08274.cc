#include <bits/stdc++.h>
using namespace std;
const int mod = 1e7 + 9;

// cache数组 数组不超过20位 值不超过10 以及两位limit
int dp[20][10][2];

int solve(long long num) {
    if (num == 0) {
        return 0;
    }
    string s = to_string(num); // 数组转string 不是很难
    int n = s.length();
    memset(dp, -1, sizeof(dp));

    // 因为这里只考虑最大值 所以前面填了0其实也无所谓？
    function<int(int, int, int)> f = [&](int i, int mx, int lim) {
        if (i == n) {
            return mx;
        }
        if (dp[i][mx][lim] != -1) {
            return dp[i][mx][lim];
        }
        int up = lim ? s[i] - '0' : 9;
        int ans = 0;
        for (int j = 0; j <= up; j++) {
            ans += f(i + 1, max(mx, j), lim && (j == up));
            ans %= mod;
        }
        dp[i][mx][lim] = ans;
        return ans;
    };
    return f(0, 0, 1);
}

int main() {
    long long l, r;
    cin >> l >> r;
    int result = (solve(r) - solve(l - 1) + mod) % mod;
    cout << result << endl;
    return 0;
}
