from collections import Counter

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7

        freq = Counter(arr)
        values = sorted(freq)
        ans = 0

        for i, x in enumerate(values):
            for y in values[i:]:
                z = target - x - y

                if z < y or z not in freq:
                    continue

                # x < y < z
                if x < y < z:
                    ans += freq[x] * freq[y] * freq[z]

                # x == y < z
                elif x == y < z:
                    ans += (
                        freq[x] * (freq[x] - 1) // 2
                    ) * freq[z]

                # x < y == z
                elif x < y == z:
                    ans += freq[x] * (
                        freq[y] * (freq[y] - 1) // 2
                    )

                # x == y == z
                else:
                    ans += (
                        freq[x]
                        * (freq[x] - 1)
                        * (freq[x] - 2)
                        // 6
                    )

        return ans % MOD