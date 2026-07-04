class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        ans = 0
        
        for x in s:
            if x-1 not in s:
                cx = x
                l = 1

                while cx+1 in s:
                    l+=1
                    cx+=1
                
                ans = max(ans,l)
        
        return ans