class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = defaultdict(int)
        for ch in magazine:freq[ch]+=1
        for ch in ransomNote:
            freq[ch]-=1
            if freq[ch]<0:
                return False
        return True
        
        