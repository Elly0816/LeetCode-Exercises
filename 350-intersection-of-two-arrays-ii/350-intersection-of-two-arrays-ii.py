class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # items that appear in both lists
        intersect = []
        i = 0
        j = 0
        while i < len(nums1):
            while j < len(nums2):
                if i >= len(nums1) or j >= len(nums2):
                    return intersect
                if nums1[i] == nums2[j]:
                    intersect.append(nums1[i])
                    nums1.pop(i)
                    nums2.pop(j)
                    j = 0
                    continue
                j += 1
            i += 1
            j = 0
        return intersect
                    