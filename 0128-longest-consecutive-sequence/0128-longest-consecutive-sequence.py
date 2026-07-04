class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        if n==0:
            return 0
        l = {}

        for num in nums:
            if num-1 not in nums:
                l[num] = 1
                while num+1 in nums:
                    l[num+1] = l[num]+1
                    num+=1
                
        return max([v for k,v in l.items()])

        