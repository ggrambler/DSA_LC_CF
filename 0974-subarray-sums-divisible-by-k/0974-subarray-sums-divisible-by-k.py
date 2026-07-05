class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        n = len(nums)

        prefix = [0 for _ in range(n)]
        prefix[0] = (nums[0]%k)
        for i in range(1,n):
            prefix[i] = (prefix[i-1]+nums[i])%k
        prefix.insert(0,0)

        s = defaultdict(int)
        for p in prefix: s[p]+=1

        count = 0
        for k,v in s.items():
            count+=(v*(v-1)//2)

        return count
