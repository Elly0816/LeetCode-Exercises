/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    let counter = {};
    let result = [];
    for (let num of nums1){
        if (counter[num]){
            counter[num] += 1;
        } else {
            counter[num] = 1;
        }
    }
    for (const num of nums2){
        if (counter[num] > 0){
            counter[num] -= 1;
            result.push(num);
        }
    }
    return result;
}