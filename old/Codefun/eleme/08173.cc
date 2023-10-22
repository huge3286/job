#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

void solve() {
    int n, m, q;  // 地点数、路径数和需要送达旗帜的地点数
    cin >> n >> m >> q;
    vector<vector<pair<int, long long>>> g(n+1);  // 领接表
    for (int i = 0; i < m; ++i) {
        int u, v, w;
        cin >> u >> v >> w;
        g[u].emplace_back(v,w);
        g[v].emplace_back(u,w);
    }
    vector<int> tar(q);  // 目标
    for (int i = 0; i < q; ++i) {
        cin >> tar[i];
    }
    vector<long long> dis(n+1, LONG_MAX);  // 距离
    // dijkstra的核心 优先队列 存储路径长度和对应的节点
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> pq;
    pq.emplace(0,1);
    dis[1] = 0;
    while (!pq.empty()){
        // 弹出当前的最优路径和对应节点
        auto [d,u] = pq.top();
        pq.pop();
        for (auto [v, w]: g[u]){
            // 更新最优节点所有邻居的路径
            if (d + w < dis[v]){
                dis[v] = d + w;
                pq.emplace(dis[v],v);
            }
        }
    }
    long long ans = 0;
    for (int i = 0; i < q; i++)
        ans += dis[tar[i]];
    cout << ans * 2 << endl;
}

int main() {
    // 背公式 提高读取效率
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int T = 1;
    while (T--) {
        solve();
    }

    return 0;
}
