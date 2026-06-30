class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = sum([1 if x==val else 0 for x in nums])
        n = len(nums)

        l = 0
        r = n-1

        while l<r:
            while not nums[l]==val:
                l+=1
                if l>=n: break
            while nums[r]==val and r>-1:
                r-=1
                if r<=-1: break
            if l<r:
                nums[l],nums[r] = nums[r],nums[l]
                
        return n-count
        
        