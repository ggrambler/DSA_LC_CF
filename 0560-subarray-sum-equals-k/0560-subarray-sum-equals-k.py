class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count=0
        sd = defaultdict(int)
        sd[0] = 1
        ss=  0

        for x in range(0,n):
            ss+=nums[x]
            count+= sd[ss-k]
            sd[ss]+=1

        return count
        