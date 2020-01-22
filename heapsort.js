function heapify(input) {
  if (input.length <= 1)
    return;

  let index = input.length - 1;
  while (index > 0) {
    const parent = parseInt((index-1)/2);
    if (input[index] > input[parent]) {
      swap(input, index, parent);
    }
    index--;
  }
}

function swap(input, index1, index2) {
  const temp = input[index1];
  input[index1] = input[index2];
  input[index2] = temp;
}

function siftDown(arr, maxIndex) {
  let index = 0;
  do {
    let left = 2*index + 1;
    let right = 2*index + 2;
    let largest = index;
    // get largest child
    if (left < maxIndex && arr[left] > arr[index])
      largest = left;
    if (right < maxIndex && arr[right] > arr[largest])
      largest = right;
    if (largest == index)
      break;
    swap(arr, index, largest);
    console.log(arr);
    index = largest;
  } while (index <= maxIndex);
}

function heapSort(arr) {
  if (arr.length <= 1)
    return;

  let index = arr.length - 1;
  heapify(arr);
  console.log('heapify:');
  console.log(arr);

  while (index > 0) {
    swap(arr, 0, index);
    index--;
    siftDown(arr, index);
  }
}

// tests
const input = [6, 5, 3, 1, 8, 7, 2, 4];
// heapify(input);
// siftUp(input, input.length -1);

heapSort(input);
console.log('After sorting:');
console.log(input);
