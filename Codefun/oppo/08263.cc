#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    int n;
    cin >> n;
    string a;
    cin >> a;

    vector<vector<int>> g(n, vector(n, 0));
    vector<int> o(n, 0);

    while (n--) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
        o[u] += a[v] == 'o' ? 1 : 0;
        o[v] += a[u] == 'o' ? 1 : 0;
    }

    function<int(int, int)> f;
    f = [&](int x, int z)-> int
    {
        int res = 0;
        if (z != 1 && a[x] == 'p' && a[z] == 'p') {
            res += o[x] * o[z];
        }

        for (int y: g[x]) {
            if (y == z) {
                continue;
            }
            res += f(y, x);
        }

        return res;
    };

    int ans = f(0, -1) * 2;
    cout << ans << endl;
    return 0;
}