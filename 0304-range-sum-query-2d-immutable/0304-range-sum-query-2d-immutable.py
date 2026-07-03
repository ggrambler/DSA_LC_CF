class NumMatrix:
    
    def __init__(self, m: List[List[int]]):
        r = len(m)
        c = len(m[0])
        self.summ = [[0 for _ in range(c)] for __ in range(r)]
        self.summ[0][0] = m[0][0]
        for i in range(1,r):
            self.summ[i][0] = self.summ[i-1][0]+m[i][0]
        for j in range(1,c):
            self.summ[0][j] = self.summ[0][j-1]+m[0][j]
        for i in range(1,r):
            for j in range(1,c):
                self.summ[i][j] = self.summ[i-1][j]+self.summ[i][j-1]-self.summ[i-1][j-1]+m[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.summ[row2][col2]
        b = self.summ[row1-1][col2] if row1-1>=0 else 0
        c = self.summ[row2][col1-1] if col1-1>=0 else 0
        d = self.summ[row1-1][col1-1] if row1-1>=0 and col1-1>=0 else 0
        return a-b-c+d

