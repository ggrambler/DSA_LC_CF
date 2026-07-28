class Solution:
    def isHappy(self, n: int) -> bool:
        visi = defaultdict(int)

        c = 10
        while c:
            c-=1
            if n==1 : return True
            if visi[n]==1: return False

            visi[n] = 1
            newnum = 0
            while n:
                newnum += (n%10)**2
                n = n//10
            # print(newnum)
            n =  newnum

        return False


        