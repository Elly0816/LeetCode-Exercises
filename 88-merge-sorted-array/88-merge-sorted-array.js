/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    for (let i = 0; i<nums2.length; i++){
        nums1.push(nums2[i]);
    }
    let i = 0;
    while (i < (m+n)){
        if ((nums1[i] === 0) && (nums1.length !== m+n)){
            nums1.splice(i, 1);
        } else {
            i += 1;
        }
    }
    nums1.sort((a, b) => a - b);
}