class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

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
        ans.sort(key=lambda x: x[0])

        return ans
        
        