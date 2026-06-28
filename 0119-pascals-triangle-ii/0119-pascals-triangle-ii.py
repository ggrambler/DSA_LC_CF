class Solution:
    def getRow(self, ri: int) -> List[int]:
        if ri==0:
            return [1]
        if ri==1:
            return [1,1]

        ans = [1,1]
        while(ri>1):
            n = len(ans)
            upd = []
            for i in range(0,n-1):
                upd.append(ans[i]+ans[i+1])
            ans = [1] + upd[::] + [1]
            ri-=1
        
        return ans