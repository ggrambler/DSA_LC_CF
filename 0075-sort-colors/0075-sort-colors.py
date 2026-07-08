class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        p0 = 0
        curr = 0
        p2 = n-1

        while curr<=p2:
            if nums[curr]==0:
                nums[curr],nums[p0] = nums[p0],nums[curr]
                p0+=1
                curr+=1
            elif nums[curr]==2:
                nums[curr],nums[p2] = nums[p2],nums[curr]
                p2-=1
            else:
                curr+=1
        
