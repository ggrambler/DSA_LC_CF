class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wl = s.split(" ")
        if len(wl)!=len(pattern):
            return False

        d = defaultdict(int)
        e = defaultdict(int)
        INR = 1
        for word in wl:
            if d[word]==0:
                d[word] = INR
                INR+=1
        INR = 1
        for ch in pattern:
            if e[ch]==0:
                e[ch] = INR
                INR+=1
        
        for i in range(len(pattern)):
            if d[wl[i]]!=e[pattern[i]]:
                return False

        return True
        