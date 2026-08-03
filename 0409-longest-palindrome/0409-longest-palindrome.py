class Solution:
    def longestPalindrome(self, s: str) -> int:

        ans = 0
        maxodd = 0

        freq = defaultdict(int)
        for ch in s:freq[ch]+=1

        for k,v in freq.items():
            ans = ans+v if v%2==0 else ans+v-1
            if maxodd == 0:
                if v%2==1:
                    maxodd=1
        
        return ans+maxodd


        