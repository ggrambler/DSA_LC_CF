class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0

        nums.append(0)
        for x in nums:
            if x==0:
                ans = max(ans,count)
                count = 0
            else:
                count+=1
        
        return ans

        