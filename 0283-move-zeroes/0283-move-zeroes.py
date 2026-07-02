class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(n-1):
            if nums[i]==0:
                r = i+1
                while nums[r]==0:
                    r+=1
                    if r>=n: break
                if r<n:
                    nums[i],nums[r] = nums[r],nums[i]
        