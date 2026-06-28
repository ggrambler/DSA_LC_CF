class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n = nums.size();
        int missing = n*(n+1)/2, duplicate = -1;

        // extra array

        vector <int> pres(n,0);

        for(int x:nums)
            if(pres[x-1]==0){pres[x-1] = x;missing-=x;}
            else duplicate = x;

        return {duplicate, missing};
    }
};