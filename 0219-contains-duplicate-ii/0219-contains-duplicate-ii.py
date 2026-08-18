class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapp = defaultdict(int)
        n = len(nums)
        if n==1:
            return False

        for i in range(min(n,k+1)):
            mapp[nums[i]]+=1
            # print(mapp)
            if mapp[nums[i]]>1:
                return True

        for i in range(k+1,n):
            mapp[nums[i-k-1]]-=1
            mapp[nums[i]]+=1
            if mapp[nums[i]]>1:
                return True
        return False

