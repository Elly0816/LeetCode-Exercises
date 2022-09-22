class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        for i in range(len(nums)):
            if sum(nums[left:i]) == sum(nums[i+1:right]):
                return i
        return -1