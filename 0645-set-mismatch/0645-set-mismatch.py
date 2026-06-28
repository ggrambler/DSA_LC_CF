class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = n*(n+1)//2
        t = 0
        pre = [0]*n

        for x in nums:
            if pre[x-1]==0:
                pre[x-1] = 1
                s-=x
            else:
                t = x
            # print(x,pre,s,t)
        
        return [t,s]
