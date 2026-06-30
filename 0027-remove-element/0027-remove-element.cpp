class Solution {
public:
    int removeElement(vector<int>& nums, int val){\
        int count = 0;
        for(int x:nums)if(x==val)count++;
        int n = nums.size();
        int l = 0,r = n-1;

        while(l<r){
            while(nums[l]!=val){
                l+=1;
                if(l>=n)break;
            }
            while(nums[r]==val){
                r-=1;
                if(r<0)break;
            }
            if(l<r){
                nums[r] = nums[r]+nums[l];
                nums[l] = nums[r]-nums[l];
                nums[r] = nums[r]-nums[l];
            }
        }

        return n-count;
        
    }
};