class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        r = len(m)
        c = len(m[0])
        rl = []
        cl = []

        for i in range(r):
            for j in range(c):
                if m[i][j] == 0:
                    rl.append(i)
                    cl.append(j)
        
        for i in rl:
            for j in range(c):
                m[i][j]=0;
        for i in range(r):
            for j in cl:
                m[i][j]=0;
        