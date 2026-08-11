class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        
        row = len(mat)
        col = len(mat[0])
        num = row*col-1

        lb = 0
        rb = col
        tb = 0
        bb = row
        d = [0,+1]

        def nextstep(r,c):
            nonlocal lb,rb,tb,bb,d

            nr = r+d[0]
            nc = c+d[1]
            
            if nc>=rb:
                d = [+1,0]
                nc-=1
                nr+=d[0]
                tb+=1
            elif nr>=bb:
                d = [0,-1]
                nr-=1
                nc+=d[1]
                rb-=1
            elif nc<lb:
                d = [-1,0]
                nc +=1
                nr+=d[0]
                bb-=1
            elif nr<tb:
                d = [0,+1]
                nc+=d[1]
                nr+=1
                lb+=1
        
            return (nr,nc)
        
        ans = [mat[0][0]]

        r = c = 0
        while num:
            r,c = nextstep(r,c)
            ans.append(mat[r][c])
            num-=1

        return ans