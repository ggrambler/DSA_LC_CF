class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return 0 if s.isspace() else len(s.split()[-1])
        