class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [k for k,v in (collections.Counter(nums1) & collections.Counter(nums2)).items()]
        