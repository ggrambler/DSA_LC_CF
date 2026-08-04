class Solution:
    def getHint(self, sec: str, gg: str) -> str:

        pob = []
        cows = 0

        for i in range(len(sec)):
            if sec[i]==gg[i]:
                pob.append(i)

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for ch in sec:freq1[ch]+=1
        for ch in gg:freq2[ch]+=1

        s = set()
        for ch in sec:s.add(ch)
        for ch in s:cows+=min(freq1[ch],freq2[ch])
        
        return str(len(pob))+"A"+str(cows-len(pob))+"B"
        