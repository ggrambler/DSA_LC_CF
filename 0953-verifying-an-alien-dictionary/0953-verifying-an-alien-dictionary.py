class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)

        value = {}
        for i in range(len(order)):
            value[order[i]] = 26-i
        # print(value)

        def cmp(worda,wordb):
            # print('called', worda,wordb,len(worda),len(wordb))

            alen = len(worda)
            blen = len(wordb)

            nn = min(alen,blen) 

            start = 0
            while start<nn:
                # print(worda[start])
                if value[worda[start]]>value[wordb[start]]:
                    return True
                elif value[worda[start]]==value[wordb[start]]:
                    start+=1
                    continue
                else:
                    return False
                return False
            
            if alen>blen:
                return False

            return True
        
        for i in range(n-1):
            if not cmp(words[i],words[i+1]):
                return False

        return True
        