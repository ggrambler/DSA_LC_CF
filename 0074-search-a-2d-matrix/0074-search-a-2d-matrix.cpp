class Solution {
private:
    bool bins(vector<int> arr,int x){
        int low = 0;
        int high = arr.size();
        
        while(low<high){
            int mid = (high-low)/2+low;
            cout<<low<<" "<<mid<<" "<<high<<endl;
            if(arr[mid]==x)return true;
            if(arr[mid]>x){high = mid;}
            if(arr[mid]<x){low = mid+1;}
        }

        return false;
    }
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        
        int r = matrix.size();
        int c = matrix[0].size();

        for(int i=0;i<r;i++){
            if(target<=matrix[i][c-1]){
                return bins(matrix[i],target);
                break;
            }
        }
        return false;
    }
};