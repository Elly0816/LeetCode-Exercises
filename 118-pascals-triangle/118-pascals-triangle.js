/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const triangle = [];
    for (let i=0; i<numRows; i++){
        triangle.push([]);
    }
    for (let i=0; i<triangle.length; i++){
        if (i===0){
            triangle[0].push(1);
        } else {
            for(let j=0; j<=i; j++){
                if((!triangle[i-1][j-1]) || (!triangle[i-1][j])) {
                    triangle[i].push(1);
                } else {
                    triangle[i].push(triangle[i-1][j-1] + triangle[i-1][j]);
                }
            }
        }
    }
    return triangle;
};