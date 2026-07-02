class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        while k:
            val = nums.pop(n-1)
            nums.insert(0,val)
            k-=1
        