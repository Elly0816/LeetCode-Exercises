class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # items that appear in both lists
        intersect = []
        # Using a counter to store the data as a dictionary with key = item and value = number of times it appears
        c = Counter(nums1)
        for n in nums2:
            if c[n] > 0:
                c[n] -= 1
                intersect.append(n)
        return intersect