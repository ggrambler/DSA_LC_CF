class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c= 0 
        s = s+" "
        ans = 0

        for ch in s:
            if ch==" ":
                if c>0:
                    ans = c
                c=0
            else:
                c+=1
        
        return ans