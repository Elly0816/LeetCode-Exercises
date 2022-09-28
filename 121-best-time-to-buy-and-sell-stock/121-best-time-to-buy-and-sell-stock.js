/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let currDiff = 0;
    let maxDiff = 0;
    const length = prices.length;
    let buy = 0;
    let sell = 1;
    
    while (sell < length){
        //Check if the difference is greater than the current difference
        if (prices[sell] - prices[buy] > currDiff){
            currDiff = prices[sell] - prices[buy];
        }
        
        if (prices[sell] < prices[buy]){
            buy = sell;
        } else {
            maxDiff = Math.max(currDiff, maxDiff);
        }
        
        sell ++;
        
    }
    
    return maxDiff;
}