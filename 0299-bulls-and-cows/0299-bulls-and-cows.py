from collections import Counter

class Solution:
    def getHint(self, sec: str, gg: str) -> str:

        bull = sum([1 if sec[i]==gg[i] else 0 for i in range(len(sec))])

        cows = 0
        freq1 = Counter(sec)
        freq2 = Counter(gg)

        for ch,v in freq1.items():
            cows+=min(freq1[ch],freq2[ch])
        
        return str(bull)+"A"+str(cows-bull)+"B"
        