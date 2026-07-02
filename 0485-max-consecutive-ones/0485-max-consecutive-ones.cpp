class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums){
        int ans = 0,count = 0;

        for(int x:nums){
            if(x==1)count+=1;
            if(x==0)count=0;
            if(ans<count)ans=count;
        }
        return ans;
    }
};