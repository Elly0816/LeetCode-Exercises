/**
 * @param {number[][]} mat
 * @param {number} r
 * @param {number} c
 * @return {number[][]}
 */
var matrixReshape = function(mat, r, c) {
    let m = mat.length;
    let n = mat[0].length;
    let inner = [];
    let outer = [];
    if (m*n !== r*c){
        return mat;
    } else {
        for(let i=0; i<m; i++){
            for (let j=0; j<n; j++){
                if (inner.length < c){
                    inner.push(mat[i][j]);
                } else {
                    outer.push(inner);
                    inner = [];
                    inner.push(mat[i][j]);
                }
            }
        }
        if (outer.length < r){
            outer.push(inner);
        }
        return outer;
    }
};