class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        valid = [0]*(n+1)

        for num in nums:
            if 0<num<=n:
                valid[num]=1
        for x in range(1,n+1):
            if valid[x]==0:
                return x
                
        return n+1