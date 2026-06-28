class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(), idx2 = 0;
        map <int,int> mapp;

        for(int i=0;i<n;i++){
            if(mapp.find(target - nums[i]) != mapp.end())return {mapp[target - nums[i]],i};
            mapp[nums[i]] = i;
        }
        
        return {};
    }
};