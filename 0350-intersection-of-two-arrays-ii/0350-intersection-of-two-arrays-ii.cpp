class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {

        map <int,int> mapp;
        for(auto x:nums1)mapp[x]++;
        vector <int> ans;
        for(auto x:nums2){
            if(mapp[x]>0){
                mapp[x]--;
                ans.push_back(x);
            }
        }
        return ans;
    }
};