class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        nums = arr[::]

        arr.sort()

        ans = []

        rank = {}
        rr = 1
        seen = set()
        for i in range(n):
            num = arr[i]
            if num not in seen:
                seen.add(num)
                rank[num] = rr
                rr+=1
        for num in nums:
            ans.append(rank[num])        

        return ans
        