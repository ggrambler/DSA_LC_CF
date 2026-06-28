class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums){
        // brute force

        int missing = -1;
        int duplicate = -1;
        int n = nums.size();

        map <int,int> mapp;
        for(int x:nums)mapp[x]++;

        for(int x = 1;x<=n;x++){
            if(mapp[x]==0)missing = x;
            if(mapp[x]==2)duplicate = x;
        }

        return {duplicate,missing};
        
    }
};