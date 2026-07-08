class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1],nums[0]+nums[1])

        allneg = True
        for num in nums:
            if num>=0:
                allneg = False
                break
        
        if allneg:
            return max(nums)

        ans = 0
        maxsum = 0

        for num in nums:
            maxsum+=num
            if maxsum<0:
                maxsum = 0
            ans = max(ans,maxsum)
        
        return ans
        