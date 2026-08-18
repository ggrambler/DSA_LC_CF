class Solution:
    def findMin(self, nums: List[int]) -> int:

        def minele(nums):
            n = len(nums)
            if n<4: return min(nums)
            mid = n//2
            

            opt = 0
            if nums[0]<nums[mid]:opt+=1  
            if nums[-1]<nums[mid]:opt+=2
    
            print(nums,n,mid,opt)
                
            if opt==3:
                if nums[0]<nums[-1]:
                    opt = 1
                else:
                    opt = 2
            if opt==0:return min(nums[mid],minele(nums[:mid]),minele(nums[mid+1:]))
            if opt==1:return minele(nums[:mid])
            if opt==2:return minele(nums[mid+1:])


        return minele(nums)
        


        