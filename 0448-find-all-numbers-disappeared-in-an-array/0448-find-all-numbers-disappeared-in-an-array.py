class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        ans = []
        n = len(nums)

        for i in range(n):
            idx = abs(nums[i])-1
            nums[idx] = -(abs(nums[idx]))

        for i in range(n):
            if nums[i]>0:
                ans.append(i+1)

        return ans

        