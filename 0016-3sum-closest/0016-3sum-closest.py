class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        ans = float('inf')
        diff = float('inf')

        for i in range(n):
            l = i+1
            r = n-1

            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s==target:
                    return target
                elif s<target:
                    l+=1
                else:
                    r-=1
                
                gap = abs(target-s)
                if gap<diff:
                    diff = gap
                    ans = s
        
        return ans
        