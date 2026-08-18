from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        a = Counter(s)
        b = Counter(t)
        for k in a:
            if a[k]!=b[k]:
                return False
        return True

        