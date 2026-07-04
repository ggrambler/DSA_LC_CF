class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        base = 0 # count / total sum 
        le = [-1 for i in range(n+1)]  # for storing ower bound for each sum
        ue = [-1 for i in range(n+1)]   # for upper bound of each sum
        le[0] = 0

        for i in range(n):
            base = base-1 if nums[i]==0 else base+1
            if le[base]==-1:
                le[base] = i+1
            elif le[base]!=-1:
                ue[base] = i+1

            ans = max(ans,ue[base]-le[base])
            
        return ans     