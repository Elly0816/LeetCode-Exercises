class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #Save the first value of the array as the max sum
        current_max = nums[0]
        global_max = current_max
        #Check for the larger sub array ending in the nth index
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max+nums[i])
            # check if the current max is greater than the global max
            if current_max > global_max:
                global_max = current_max
        return global_max
            
        
        