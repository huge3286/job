#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        /*
        实际上是在寻找前k个元素 k = (n-1) / 2
        1. 在nums1中取k1个 则在nums2中取k2=n-k1个元素
        2. nums1[k1] > nums2[k2-1] && nums1[k1-1] < nums1[k2] 我们要找到这样的k1和k2
        3. 如果 nums1[k1] < nums2[k2-1] 说明k1太小了
        */
        
        if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
        const int n1=nums1.size(), n2=nums2.size(), n=n1+n2, k=(n+1)/2 ;
        
        // 二分确定边界
        int l = 0, r = n1 - 1;
        while (l <= r) {
            int m = (r - l) / 2 + l;
            if (nums1[m] < nums2[k - m -1]) 
                l = m + 1;
            else 
                r = m - 1;
        }
        const int k1 = l, k2 = k-l;

        double m1 = max(k1<=0 ? -1e6:nums1[k1-1], k2<=0 ? -1e6:nums2[k2-1]);
        if (n&1 == 1) return m1; 

        double m2 = min(k1>=n1 ? 1e6:nums1[k1], k2>=n2 ? 1e6:nums2[k2]);
        return (m1+m2)/2;
    }
};