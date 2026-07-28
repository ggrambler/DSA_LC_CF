class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)

        value = {}
        for i in range(len(order)): value[order[i]] = 26-i

        def cmp(worda,wordb):
            alen,blen = len(worda),len(wordb)

            start = 0
            while start<min(alen,blen):
                if value[worda[start]]>value[wordb[start]]:
                    return True
                elif value[worda[start]]==value[wordb[start]]:
                    start+=1
                    continue
                return False
            if alen>blen: return False
            return True
        
        for i in range(n-1):
            if not cmp(words[i],words[i+1]):
                return False

        return True
        