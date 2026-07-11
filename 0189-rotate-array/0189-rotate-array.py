class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        count = 0
        start = 0

        while count < n:
            curr = start
            stored = nums[start]
            while True:
                nxt = (curr + k) % n
                nums[nxt], stored = stored, nums[nxt]
                curr = nxt
                count += 1
                # print(curr,stored,nums)

                if curr == start:
                    break

            start += 1