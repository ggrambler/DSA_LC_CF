
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int r = board.size();
        int c = board[0].size();
        vector <vector<int>> newboard(r,vector<int>(c,0));
        if(r==1 && c==1){
            board[0][0] = 0;
            return;
        };

        if(r==1){
            for(int j=0;j<c;j++){
                int curr_cell = board[0][j];
                int count = 0;

                if(j==0)count = board[0][j+1];
                else if(j==c-1)count = board[0][j-1];
                else count= board[0][j-1]+board[0][j+1];

                if(curr_cell==1 && count==2)newboard[0][j]=1;
                if(curr_cell==1 && count==3)newboard[0][j]=1;
                if(curr_cell==0 && count==3)newboard[0][j]=1;

            }
            for(int i=0;i<r;i++){for(int j=0;j<c;j++)board[i][j] = newboard[i][j];}
            return;
        }
        if(c==1){
            for(int i=0;i<r;i++){
                int curr_cell = board[i][0];
                int count = 0;

                if(i==0)count = board[i+1][0];
                else if(i==r-1)count = board[i-1][0];
                else count= board[i+1][0]+board[i-1][0];

                if(curr_cell==1 && count==2)newboard[i][0]=1;
                if(curr_cell==1 && count==3)newboard[i][0]=1;
                if(curr_cell==0 && count==3)newboard[i][0]=1;
            }
            for(int i=0;i<r;i++){for(int j=0;j<c;j++)board[i][j] = newboard[i][j];}
            return;
        }

        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                int curr_cell = board[i][j];
                int count = 0;

                if(i==0 && j==0)count = board[0][1] + board[1][0] + board[1][1];
                else if(i==0 && j==c-1)count = board[i][j-1]+board[i+1][j-1]+board[i+1][j];
                else if(i==r-1 && j==0)count = board[i-1][j]+board[i-1][j+1]+board[i][j+1];
                else if(i==r-1 && j==c-1)count = board[i-1][j-1]+board[i][j-1]+board[i-1][j];
                else if(i==0)count = board[i][j-1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]+board[i][j+1];
                else if(i==r-1)count = board[i-1][j-1]+board[i][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j+1];
                else if(j==0)count = board[i-1][j]+board[i+1][j]+board[i-1][j+1]+board[i+1][j+1]+board[i][j+1];
                else if(j==c-1)count = board[i-1][j-1]+board[i][j-1]+board[i+1][j-1]+board[i-1][j]+board[i+1][j];
                else{
                    count = board[i-1][j-1]+board[i][j-1]+board[i+1][j-1]+board[i-1][j]+board[i+1][j]+board[i-1][j+1]+board[i+1][j+1]+board[i][j+1];
                }

                if(curr_cell==1 && count==2)newboard[i][j]=1;
                if(curr_cell==1 && count==3)newboard[i][j]=1;
                if(curr_cell==0 && count==3)newboard[i][j]=1;
                // cout<<board[i][j]<<" "<<count<<" "<<newboard[i][j]<<endl;
            }
        }            
        for(int i=0;i<r;i++){for(int j=0;j<c;j++)board[i][j] = newboard[i][j];}


    }
};