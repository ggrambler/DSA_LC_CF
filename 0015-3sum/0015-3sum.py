class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)


        for i in range(n):
            
            if i>0 and nums[i-1]==nums[i]:
                continue
            
            l = i+1
            r = n-1

            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and nums[r+1]==nums[r]:
                        r-=1

                elif s<0:
                    l+=1
                else:
                    r-=1


        
        return ans