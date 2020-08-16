function mergeSort(input) {
  if (input.length <= 1)
    return input;
  const index = parseInt(input.length / 2);
  let right = input.splice(index);
  const la = mergeSort(input);
  const ra = mergeSort(right);
  let newArr = merge(la, ra);

  return newArr;
}

function merge(left, right) {
  let leftIndex = 0;
  let rightIndex = 0;
  const result = [];

  while(leftIndex < left.length && rightIndex < right.length) {
    const le = left[leftIndex];
    const re = right[rightIndex];
    if (le <= re) {
      result.push(le);
      leftIndex++;
    } else {
      result.push(re);
      rightIndex++;
    }
  }

  while (leftIndex < left.length) {
      result.push(left[leftIndex++]);
  }

  while (rightIndex < right.length) {
      result.push(right[rightIndex++]);
  }

  return result;
}

let input = [3, 1, 23, 2, 235, 88, 634, 27, 73, 56, 89, 14, 22];
let sorted = mergeSort(input);
console.log(`sorted array: ${sorted}`);

input = [1, 2, 3, 4 , 5];
sorted = mergeSort(input);
console.log(`sorted array: ${sorted}`);
