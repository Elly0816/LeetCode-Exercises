class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = []
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            sum.append(current_sum)
        return sum