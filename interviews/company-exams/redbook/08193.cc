#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> PLL;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    vector<ll> h(n), t(n);
    for (int i = 0; i < n; ++i) cin >> h[i];
    for (int i = 0; i < n; ++i) cin >> t[i];

    // 建图
    vector<vector<PLL>> g(n);
    for (int i = 0; i < m; ++i) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        u--; v--;
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }

    ll ans = 0;
    // 一个点
    for (int i = 0; i < n; ++i) {
        if (t[i] <= k) {
            ans = max(ans, h[i]);
        }
    }

    // 两个点
    for (int i = 0; i < n; ++i) {
        for (auto& [j, w]: g[i]) {
            if (w + t[i] + t[j] <= k) {
                ans = max(ans, h[i] + h[j]);
            }
        }
    }

    // 枚举中间点 再找到两个邻居即可
    for (int i = 0; i < n; ++i) {
        vector<PLL> vec;
        // 枚举中间点的所有邻居
        for (auto& [j, w]: g[i]) {
            // 构建(总耗时, 快乐值)
            vec.emplace_back(w + t[j], h[j]);
        }
        // 按照总耗时排序
        sort(vec.begin(), vec.end());

        // 枚举其中一个邻居
        for (int x = 1; x < int(vec.size()); ++x) {
            // 利用二分法找到对于 upper_bound k 的最大元素
            int l = 0, r = x - 1;
            while (l < r) {
                int mid = (l + r + 1) >> 1;
                if (vec[mid].first + vec[x].first + t[i] <= k) {
                    l = mid;
                } else {
                    r = mid - 1;
                }
            }

            // 按照 耗时最大更新数值 (这是不合逻辑的)
            if (vec[l].first + vec[x].first + t[i] <= k) {
                ans = max(ans, h[i] + vec[x].second + vec[l].second);
            }

            // 如果 x 满足条件 那么 x 之前的元素肯定都满足 
            // 冒泡排序 保存 x 之前元素快乐值最大值
            vec[x].second = max(vec[x].second, vec[x - 1].second);
        }
    }

    cout << ans << "\n";

    return 0;
}
