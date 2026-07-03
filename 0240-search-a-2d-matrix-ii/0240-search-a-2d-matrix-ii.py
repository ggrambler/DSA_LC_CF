class Solution:
    def searchMatrix(self, g: List[List[int]], x: int) -> bool:
        if not g : return False
        r = len(g)
        c = len(g[0])

        def recs(l,u,r,d):
            if l>r or u>d:
                return False
            elif x<g[u][l] or x>g[d][r]:
                return False
            mid = (r-l)//2 + l

            row = u
            while row<=d and g[row][mid] <= x:
                if g[row][mid] ==x: return True
                row+=1
            
            return recs(l,row,mid-1,d) or recs(mid+1,u,r,row-1)

        return recs(0,0,c-1,r-1)



        