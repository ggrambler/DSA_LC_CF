class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        # brute force
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        # return []

        # one pass -> hashmap

        mapp = {}

        for idx in range(n):
            num = nums[idx]
            if mapp.get(target - num,-1) > -1:
                return [mapp[target - num],idx]
            mapp[num] = idx
        
        return []