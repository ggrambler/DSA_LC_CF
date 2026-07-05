class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(1,n):
            val = nums[i]-nums[i-1]
            if val>0:
                ans+=val

        return ans
        