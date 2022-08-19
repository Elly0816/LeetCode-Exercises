class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # make the arrays of the length provided
        # merge both arrays and sort them
        while len(nums1) != m:
            nums1.pop()
        nums1 += nums2
        nums1.sort()
        
