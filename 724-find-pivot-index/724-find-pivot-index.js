/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let left = 0;
    let right = nums.reduce((total, current) => {return total+current}, 0);
    for (let i=0; i<nums.length; i++){
        right -= nums[i];
        if (right === left){
            return i;
        }
        left += nums[i];
    };
    return -1;
};