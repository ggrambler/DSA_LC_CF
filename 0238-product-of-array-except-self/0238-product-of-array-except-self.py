class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lp = []
        rp = []

        slp = 1
        rlp = 1

        n = len(nums)

        for i in range(n):
            slp*=nums[i]
            rlp*=nums[n-1-i]
            lp.append(slp)
            rp.insert(0,rlp)
        
        # print(nums,lp,rp,sep='\n')

        ans = []

        for i in range(n):
            if i==0:
                ans.append(rp[i+1])
            elif i==n-1:
                ans.append(lp[i-1])
            else:
                ans.append(lp[i-1]*rp[i+1])

        return ans