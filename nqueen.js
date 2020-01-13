var totalNQueens = function(n) {
    const cols = {};
    const diag1 = {};
    const diag2 = {};
    
    function helper(row, count, n) {
        for (let col = 0; col < n; col++) {
            if (cols[col]) continue;
            const sum = row + col;
            const sub = row - col;
            if (diag1[sum]) continue;
            if (diag2[sub]) continue;
            
            if (row == n - 1) {
                count++;
            } else {
                cols[col] = true;
                diag1[sum] = true;
                diag2[sub] = true;
                count = helper(row + 1, count, n);
                delete cols[col];
                delete diag1[sum];
                delete diag2[sub];
            }
        }
        return count;
    }
    
    return helper(0, 0, n);
};

let n = 8;
let r = totalNQueens(n);
console.log(`result for [${n}*${n}] is ${r}.`);