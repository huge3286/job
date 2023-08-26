#include <bits/stdc++.h>
using namespace std;
// 利用递归的层级结构 来从底层开始往回递推dp数组

void solve() {
    int n;
    cin >> n;
    vector<vector<int>>g(n);
    for (int i = 0; i < n-1; i++) {
        int u,v;
        cin >> u >> v;
        u--, v--;
        g[u].push_back(v);
        g[v].push_back(u);
    }
    // dp[i]表示节点i能吃到脑子的个数，nxt[i]表示i要传送到下一个的节点编号
    int dp[n], nxt[n];
    // 这个函数就是返回最小的节点编号
    function<int(int, int)> dfs = [&] (int x, int fa) ->int{
        // mi表示最小节点编号 初始化为1e6
        int mi = 1e6;
        // 先递归到最底层 拿到最小序号
        for(int y : g[x]) {
            if(y == fa) continue;
            mi = min(mi, dfs(y, x));
        }
        // mi是节点x要传送到的下一个节点
        nxt[x] = mi;
        // 如果该节点是叶子节点
        if(nxt[x] == 1e6) 
            dp[x] = 1;
        else    // 如果不是叶节点，就继续往下搜索
            dp[x] = dp[nxt[x]] + 1;
        return min(x,mi);   // 返回子树中编号最小的节点
    };
    dfs(0,-1);
    for(int i = 0; i < n; i++)
        cout << dp[i] << " ";
}   

int main() {
    solve();
    return 0;
}
