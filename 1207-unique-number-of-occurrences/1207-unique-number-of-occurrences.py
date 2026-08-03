class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freq = defaultdict(int)
        for x in arr:
            freq[x]+=1
        
        cof = defaultdict(int)
        for k,v in freq.items():
            if cof[freq[k]]>0 :
                return False
            cof[freq[k]]+=1
        
        return True