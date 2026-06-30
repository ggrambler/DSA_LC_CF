class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        if n<3:
            return 0

        l = 0
        r = 0
        mp = {'a':0,'b':0,'c':0}
        ans = 0

        while r<n:
            mp[s[r]]+=1
            r+=1
            while(mp['a']>0 and mp['b']>0 and mp['c']>0):
                ans += (n-r+1)
                mp[s[l]]-=1
                l+=1
            #     print("WHILE ",l,r,mp,ans)
            # print(l,r,mp,ans)
    
        return ans

