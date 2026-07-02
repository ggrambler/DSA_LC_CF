
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        INTMAX = 1024
        r = len(grid)
        c = len(grid[0])

        mincost = [[ INTMAX for _ in range(c)] for _ in range(r)]
        q = [(0,0)]
        mincost[0][0] = grid[0][0]

        dirs = [(-1,0),(0,+1),(+1,0),(0,-1)]

        while q:
            n,m = q.pop(0)
            cost = mincost[n][m]
            for ra,ca in dirs:
                nr = n+ra
                nc = m+ca
                if 0<=nr<r and 0<=nc<c:
                    if mincost[nr][nc] > mincost[n][m]+grid[nr][nc]:
                        q.append((nr,nc))
                        mincost[nr][nc] = mincost[n][m]+grid[nr][nc]

        return mincost[r-1][c-1] < health