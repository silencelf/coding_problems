function heapify(input, count) {
  let start = parseInt((count-2)/2);
  while (start >= 0) {
    siftDown(input, start, count-1);
    start--;
  }
}

function swap(input, index1, index2) {
  const temp = input[index1];
  input[index1] = input[index2];
  input[index2] = temp;
}

function siftDown(arr, start, end) {
  let index = start;
  do {
    let left = 2*index + 1;
    let right = 2*index + 2;
    let largest = index;
    // get largest child
    if (left <= end && arr[left] > arr[index])
      largest = left;
    if (right <= end && arr[right] > arr[largest])
      largest = right;
    if (largest == index)
      break;
    swap(arr, index, largest);
    index = largest;
  } while (index <= end);
  console.log('after siftdown:');
  console.log(arr);
}

function heapSort(arr) {
  let index = arr.length - 1;
  heapify(arr, arr.length);
  console.log('after heapify:');
  console.log(arr);
  while (index > 0) {
    swap(arr, 0, index);
    index--;
    siftDown(arr, 0, index);
  }
}

// tests
let input = [6, 5, 3, 1, 8, 7, 2, 4];
heapSort(input);
console.log('After sorting:');
console.log(input);

console.log('---------------------------------------');
input = [];
heapSort(input);
console.log('After sorting:');
console.log(input);

console.log('---------------------------------------');
input = [1, 2, 3, 4, 5];
heapSort(input);
console.log('After sorting:');
console.log(input);
