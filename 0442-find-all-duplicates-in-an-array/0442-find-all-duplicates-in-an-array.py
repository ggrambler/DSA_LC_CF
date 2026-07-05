class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num]+=1
        ans = []
        for k,v in d.items():
            if v>1:
                ans.append(k)
        return ans