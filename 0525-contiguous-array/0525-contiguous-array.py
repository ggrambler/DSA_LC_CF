class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        base = 0
        le = [-1 for i in range(n+1)]
        ue = [-1 for i in range(n+1)]
        le[0] = 0

        for i in range(n):
            base = base-1 if nums[i]==0 else base+1
            if le[base]==-1:
                le[base] = i+1
            elif le[base]!=-1:
                ue[base] = i+1

        for i in range(n+1):
            ans = max(ans,ue[i]-le[i])
        
        return ans     