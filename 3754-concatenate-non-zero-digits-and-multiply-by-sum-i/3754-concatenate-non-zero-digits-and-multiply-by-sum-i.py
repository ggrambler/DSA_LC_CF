class Solution:
    def sumAndMultiply(self, n: int) -> int:

        newnum = 0
        sumn = 0
        i = 0

        while n:
            d = n%10
            n = n//10
            if d==0:
                continue
            newnum+=d*10**i
            sumn+=d
            i+=1

        return newnum*sumn