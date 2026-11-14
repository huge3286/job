#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    vector<int> leaf(n);
    vector<int> tree(2 * n, 0);
    vector<int> sum(2 * n, 0);
    // 二叉树的节点数是2n-1 其中n是最后一层的节点数
    vector<vector<int>> range(2 * n, vector<int>(2, 0));

    for (int i = 0; i < n; ++i) cin >> leaf[i];
    
    // DP求最大最小值
    for (int i = 2 * n - 1; i > 0; --i) {
        if (i >= n) {
            range[i][0] = leaf[i - n];
            range[i][1] = leaf[i - n];
        }
        else {
            // 这是什么道理 哦好像可以找规律
            int l = i * 2, r = i * 2 + 1;
            range[i][0] = min(range[l][0], range[r][0]);
            range[i][1] = max(range[l][1], range[r][1]);
        }
    }

    // 再往下推就行了
    for (int i = 1; i < 2 * n; ++i) {
        sum[i] += (sum[i / 2] + tree[i / 2]);
        tree[i] = (range[i][0] + range[i][1]) / 2 - sum[i];
        
    }

    for (int i = 1; i < 2 * n - 1; ++i) cout << tree[i] << " ";
    cout << tree[2 * n - 1] << endl;
    return 0;
}

