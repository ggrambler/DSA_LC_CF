class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        
        int r = grid.size();
        int c = grid[0].size();

        vector <vector<int>> mincost(r,vector<int>(c,1024));

        queue<pair<int,int>> q;
        q.push({0,0});

        mincost[0][0] = grid[0][0];

        static vector <pair<int,int>> dirs = {{+1,0},{-1,0},{0,-1},{0,+1}};

        while(q.size()>0){
            auto [n,m] = q.front();
            q.pop();
            int cost = mincost[n][m];

            for(auto x:dirs){
                int nr = n+x.first;
                int nc = m+x.second;
                if(0<=nr && nr<r && 0<=nc && nc<c){
                    if(mincost[nr][nc] > mincost[n][m]+grid[nr][nc]){
                        q.push({nr,nc});
                        mincost[nr][nc] = mincost[n][m]+grid[nr][nc];
                    }
                }
            }
        }

        return(mincost[r-1][c-1] < health);

    }
};