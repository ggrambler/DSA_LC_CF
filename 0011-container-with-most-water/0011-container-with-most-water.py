class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len(h)

        #brute force
        # ans = 0
        # for m in range(n-1,0,-1):
        #     for i in range(0,n-m):
        #         ans = max(ans,min(h[i],h[m+i])*m)
        # return ans
        
        # 2 pointer approach

        ans = 0

        l = 0
        r = n-1
        w = n-1
        
        while l<r:
            ans = max(ans,min(h[l],h[r])*w)
            if h[l]<h[r]:
                l+=1
                w-=1
            else:
                r-=1
                w-=1

        return ans
        