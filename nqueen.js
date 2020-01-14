var totalNQueens = function(n) {
    const cols = {};
    const diag1 = {};
    const diag2 = {};
    const results = [];

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

    /**
       this function traces the result path.
    **/
    function helper2(row, trace, n) {
      for (let col = 0; col < n; col++) {
        if (cols[col]) continue;
        const sum = row + col;
        const sub = row - col;
        if (diag1[sum]) continue;
        if (diag2[sub]) continue;

        if (row == n - 1) {
          trace.push(col);
          results.push([...trace]);
          trace.pop();
        } else {
          cols[col] = true;
          diag1[sum] = true;
          diag2[sub] = true;
          trace.push(col);
          helper2(row + 1, trace, n);
          trace.pop(col);
          delete cols[col];
          delete diag1[sum];
          delete diag2[sub];
        }
      }
    }

    // return helper(0, 0, n);
    helper2(0, [], n);
    return results;
};

let n = 8;
let r = totalNQueens(n);

for(let s of r) {
  for(let row of s) {
    let rowDisplay = '';
    for (let col=0; col<n; col++) {
      const symbol = col === row ? 'Q':'_';
      rowDisplay += symbol;
    }
    console.log(rowDisplay);
  }
  console.log();
}
console.log(`result for [${n}*${n}] is ${r.length}.`);
