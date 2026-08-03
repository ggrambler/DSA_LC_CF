class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        freq = defaultdict(int)

        for ch in stones:
            freq[ch]+=1
        print(freq)

        ans = 0
        for ch in jewels:
            ans+=freq[ch]
        
        return ans