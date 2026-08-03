class Solution:
    def longestPalindrome(self, s: str) -> int:

        ans = 0
        maxodd = 0

        freq = defaultdict(int)
        for ch in s:freq[ch]+=1
        print(freq)

        for k,v in freq.items():
            if v%2==0:
                ans+=v
            else:
                maxodd = 1
                ans+=(v-1)
        
        return ans+maxodd


        