class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # starting at the first number
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            # subtracts the current value from the right total
            right -= nums[i]
            # if the left and right are the same values
            if left == right:
                return i
            # add the current value to the left sum
            left += nums[i]
        return -1
        # left, right = 0, sum(nums)
        # for index, num in enumerate(nums):
        #     right -= num
        #     if left == right:
        #         return index
        #     left += num
        # return -1
        