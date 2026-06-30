class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n,m = m,n
        if m==0:
            return
        if n==0:
            nums1[:] = nums2
            return
        
        a = 0
        b = 0
        ans = []
        while a<n and b<m:
            if nums1[a]<=nums2[b]:
                ans.append(nums1[a])
                a+=1
            else:
                ans.append(nums2[b])
                b+=1
        
        while a<n:
            ans.append(nums1[a])
            a+=1
        while b<m:
            ans.append(nums2[b])
            b+=1
            
        nums1[:] = ans


        



        