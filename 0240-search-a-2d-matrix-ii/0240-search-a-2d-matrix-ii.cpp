class Solution {
public:
    bool searchMatrix(vector<vector<int>>& g, int x) {
        
        int r = g.size()-1;
        int c = 0;

        while(true){
            int lastele = g[r][c];
            if(lastele==x)return true;
            if(lastele>x){r--;}
            if(lastele<x)c++;
            if(r<0 || c>=g[0].size())break;
        }

        return false;
    }
};