class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)

        maxn = nums[0]
        minn = nums[0]

        result = maxn

        for i in range(1,n):
            maxn,minn = max(nums[i], max(maxn*nums[i], minn*nums[i])), \
                        min(nums[i], min(maxn*nums[i], minn*nums[i]))
            result = max(maxn, result)

        return result