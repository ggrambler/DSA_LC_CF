class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size(), idx2 = 0;
        map <int,int> mapp;

        for(int i=0;i<n;i++){
            if(mapp[target-nums[i]]>0){
                idx2 = i;
                break;
            }
            mapp[nums[i]] = i;
        }
        
        return {mapp[target - nums[idx2]],idx2};
    }
};