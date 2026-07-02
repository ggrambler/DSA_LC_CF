class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        insert = 0
        
        for i in range(n):
            if nums[i]!=0:
                nums[insert],nums[i] = nums[i],nums[insert]
                insert+=1
        
                
        