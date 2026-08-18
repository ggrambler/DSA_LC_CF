class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        lets = {}
        usedt = set()
        for i in range(len(s)):
            if s[i] not in lets:
                if t[i] in usedt: return False
                lets[s[i]] = t[i]
                usedt.add(t[i])
            else:
                if not lets[s[i]] == t[i]:
                    return False
        return True
        
        
