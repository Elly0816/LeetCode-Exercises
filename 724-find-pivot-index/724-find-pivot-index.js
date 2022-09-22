/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    const left = 0;
    const right = nums.length;
    for (let i=0; i<nums.length; i++){
        if (nums.slice(left, i).reduce((total, curr) => {return total + curr}, 0) === nums.slice(i+1, right).reduce((total, curr) => {return total + curr}, 0)){
            return i;
        };
    };
    return -1;
};