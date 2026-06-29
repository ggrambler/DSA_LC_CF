class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mp = defaultdict(int)
        for x in nums1:mp[x]+=1

        ans = []
        for x in nums2:
            val = mp.get(x,0)
            if val>0:
                ans.append(x)
                mp[x]-=1
        
        return ans

        