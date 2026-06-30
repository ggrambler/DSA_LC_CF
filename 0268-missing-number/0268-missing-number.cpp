class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0;
        for(int x=1;x<=nums.size();x++)ans = ans^x;
        for(int x:nums)ans = ans^x;

        return ans;
    }
};