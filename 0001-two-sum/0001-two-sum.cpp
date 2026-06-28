class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        map <int,int> mapp;
        int idx = 0,idx2 = 0;

        for(int i=0;i<n;i++){
            if(mapp[target-nums[i]]>0){
                idx2 = i;
                break;
            }
            mapp[nums[i]]++;
        }
        for(int i=0;i<idx2;i++)if(nums[i] == target - nums[idx2]) idx = i;
        
        return {idx,idx2};
    }
};