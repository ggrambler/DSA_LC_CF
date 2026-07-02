class Solution:
    def searchMatrix(self, g: List[List[int]], target: int) -> bool:

        r = len(g)
        c = len(g[0])

        for i in range(r):
            for j in range(c):
                if g[i][j]==target:
                    return True;
        return False;
        