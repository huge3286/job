#include <bits/stdc++.h>
using namespace std;

template <typename T>
void print(const T& x) {
    for (const auto& i : x) {
        cout << i << ' ';
    }
    cout << endl;
}

int minGroupsForValidAssignment(vector<int>& nums) {
    unordered_map<int, int> h;
    for (int num : nums) {
        h[num]++;
    }

    int mi = 1000000000;
    priority_queue<int> pq;
    for (auto x : h) {
        pq.push(x.second);
        mi = min(mi, x.second);
    }

    while (1) {
        int top = pq.top();
        if (top - mi <= 1) {
            break;
        }
        int t = top / 2;
        mi = min(mi, t);
        pq.pop();
        pq.push(top % 2 == 1 ? t + 1 : t);
        pq.push(t);
    }

    return pq.size();
}

int main()
{
    vector<int> nums = {3,2,3,2,3};
    minGroupsForValidAssignment(nums);
    return 0;
}