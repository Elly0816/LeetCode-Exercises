class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = first +1
        while second > first:
            for i in range(second, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]
                else:
                    second += 1
            first += 1
            second = first +1