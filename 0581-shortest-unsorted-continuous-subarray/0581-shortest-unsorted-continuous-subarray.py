class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = nums[::]
        s.sort()
        n = len(s)
        minn = 2**31
        maxn = -1

        for i in range(n):
            if nums[i]!=s[i]:
                minn = min(minn,i)
                maxn = max(maxn,i)
        ans = maxn-minn+1 

        return ans if ans>=0 else 0
        