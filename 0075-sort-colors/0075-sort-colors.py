class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = defaultdict(int)
        for x in nums:
            d[x]+=1
        i = 0
        for val in [0,1,2]:
            for x in range(d[val]):
                nums[i] = val
                i+=1

        