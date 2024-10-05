#include <bits/stdc++.h>
using namespace std;

struct node
{
    int u, v, w;
    // 端点 u , v , 权值 w
    bool operator<(const node &a) const
    {
        return w > a.w;
    }
};
int fa[1010]; // 并查集
int find(int x)
{
    return x == fa[x] ? x : fa[x] = find(fa[x]);
}
void merge(int x, int y)
{
    int fx = find(x), fy = find(y);
    if (fx != fy)
        fa[fx] = fy;
}

int main()
{
    ios::sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    vector<node> e(m + 1);
    for (int i = 1; i <= m; i++)
    {
        cin >> e[i].u >> e[i].v >> e[i].w;
    }
    for (int i = 1; i <= m; i++)
    {
        fa[i] = i;
    }
    sort(e.begin() + 1, e.end());
    int cnt = 1;
    long long ans = 0;
    for (int i = 1; i <= m; i++)
    {
        auto [u, v, w] = e[i];
        if (find(u) != find(v))
        {
            merge(u, v);
            cnt++;
            ans += w;
            if (cnt == n)
            {
                cout << ans << endl;
                return 0;
            }
        }
    }
    cout << "No solution."<< endl;
}

