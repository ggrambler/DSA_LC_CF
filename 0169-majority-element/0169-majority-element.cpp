class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        int count = 0,ans;

        for(auto num:nums){
            if(count==0){
                ans = num;
                count++;
            }else if(ans == num)count++;
            else count--;
        }

        return ans;
    }
};