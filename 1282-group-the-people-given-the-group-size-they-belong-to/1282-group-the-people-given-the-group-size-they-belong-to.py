class Solution:
    def groupThePeople(self, gg: List[int]) -> List[List[int]]:

        grp = defaultdict(list)
        for i in range(len(gg)):
            grp[gg[i]].append(i)

        ans = []
        for k,v in grp.items():
            n = len(v)
            temp = []
            for i in range(n):
                temp.append(v[i])
                if (i+1)%k==0:
                    ans.append(temp)
                    temp = []
        return ans
        