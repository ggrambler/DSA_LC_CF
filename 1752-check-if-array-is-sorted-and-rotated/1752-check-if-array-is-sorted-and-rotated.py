class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        drop = 0

        for i in range(n-1):
            if not nums[i]<=nums[i+1]:
                drop+=1
        if drop==0:
            return True
        if drop==1 and nums[n-1]<=nums[0]:
            return True
        else:
            return False
        