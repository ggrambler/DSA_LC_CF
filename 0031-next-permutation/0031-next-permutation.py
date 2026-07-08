class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        
        n = len(nums)
        ans = -1

        for idx in range(n-1,0,-1):
            if nums[idx]>nums[idx-1]:
                ans = idx
                break

        if ans==-1:
            rn = nums[::-1]
            for i in range(n):
                nums[i]=rn[i]
            return
        
        for idx in range(n-1,ans-1,-1):
            if nums[ans-1]<nums[idx]:
                nums[ans-1],nums[idx] = nums[idx],nums[ans-1]
                break
        
        sr = nums[ans:]
        sr.sort()
        for idx in range(ans,n):
            nums[idx] = sr[idx-ans]

