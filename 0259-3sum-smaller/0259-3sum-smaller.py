class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        def binary_search(j: int, required: int) -> int:
            l = j + 1
            r = n
            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] < required:
                    l = mid + 1
                else:
                    r = mid
            return l - j - 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                required = target - nums[i] - nums[j]
                ans += binary_search(j, required)

        return ans