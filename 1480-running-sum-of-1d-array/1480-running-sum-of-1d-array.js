/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    const sum = [];
    let currentSum = 0;
    for (let i=0; i<nums.length; i++){
        currentSum += nums[i];
        sum.push(currentSum);
    };
    return sum;
};