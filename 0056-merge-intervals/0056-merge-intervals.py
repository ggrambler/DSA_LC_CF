class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        #brute force
        minn = float('inf')
        maxn = float('-inf')
        points = set()

        d = defaultdict(int)
        for u,v in intervals:
            minn = min(minn,u)
            maxn = max(maxn,v)
            if u==v:
                points.add(u)
            for x in range(u,v):
                d[x] = 1

        # print(d,points)
        ans = []
        for pp in points:
            if d[pp]!=1 and d[pp-1]!=1:
                ans.append([pp,pp])

        sp = ep = None
        for idx in range(minn,maxn+2):
            if d[idx]:
                if sp==None:
                    sp = idx
                    ep = None
            else:
                if ep==None and sp!=None:
                    ep = idx
                    ans.append([sp,ep])
                    sp = None
        # print(ans)




        return ans
        
        