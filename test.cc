#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> nums){
    int n=nums.size();
    unordered_map<int,int> mp;
    for(int i=0;i<n;i++){
        mp[nums[i]]++;
    }
    int m=mp.size();
    int needNum = 0;
    for(auto it=mp.begin();it!=mp.end();it++){
        if(it->second>=m+1) it->second = m+1;
        needNum += it->second;
    }
    return needNum/2;
}

int main() {
    int n; cin >> n;
    vector<int> nums(n, 0);
    int i = 0;
    while (i<n) {
        cin >> nums[i++];
    }

    int ans = solution(nums);
    cout << ans;
    return 0;
}