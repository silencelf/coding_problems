function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

function build(start, end) {
    var result = [null]
    for(var i = start; i<=end; i++) {
        var leftNodes = build(start, i - 1);
        var rightNodes = build(i+1, end);
        for(l of leftNodes)
            for(r of rightNodes){
                let root = new TreeNode(i);
                root.left = l;
                root.right = r;    
                result.push(root)
            }
    } 
    return result
}

console.log(build(1, 3));

function mergeSort(nums) {
    if(nums.length <= 1)
        return nums;
    const pivot = Math.floor(nums.length/2);
    const ll = nums.slice(0, pivot);
    const rl = nums.slice(pivot, nums.length);
    const left = mergeSort(ll);
    const right = mergeSort(rl);
    
    return merge(left, right);
} 

function merge(left, right) {
    const result = [];
    let i = 0, j = 0;
    while (i<left.length && j < right.length) {
        if (left[i]<=right[j]) {
            result.push(left[i++]);
        } else {
            result.push(right[j++]);
        }
    }
    
    while (i < left.length) {
        result.push(left[i++]);
    }
    while (j < right.length) {
        result.push(right[j++]);
    }
    return result;
}

console.log(mergeSort([5,2,3,1]));