class Solution {
private:
    bool cmp(map <char,int>& val, string worda, string wordb){
        int lena = worda.size();
        int lenb = wordb.size();
        int min = (lena<lenb)?lena:lenb;

        int start = 0;
        while(start<min){
            if(val[worda[start]]==val[wordb[start]])start++;
            else if(val[worda[start]]>val[wordb[start]])return true;
            else return false;
        }
        if(lena>lenb) return false;
        return true;
    }
public:
    bool isAlienSorted(vector<string>& words, string order) {
        map <char,int> val;
        int v = 0;

        for(char ch:order)val[ch] = 26-v++;

        for(int i=0;i<words.size()-1;i++)if (!cmp(val,words[i],words[i+1]))return false;
        return true;
    }
};