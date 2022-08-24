/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let currentMax = 0;
    let globalMax = 0;
    let right = 1;
    let left = 0;
    while (right < prices.length){
        if (prices[right] - prices[left] > currentMax){
            currentMax = prices[right] - prices[left];
        }
        if (prices[right] > prices[left]){
            globalMax = Math.max(currentMax, globalMax);
        } else {
            left = right;
        }
        right += 1;
    }
    return globalMax;
};