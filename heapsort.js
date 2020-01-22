function heapify(input) {
  if (input.length <= 1) return;

  let index = input.length - 1;
  while (index > 0) {
    const parent = parentIndex(index);
    if (parent == null) break;

    if (input[index] > input[parent]) {
      swap(input, index, parent);
    }
    index--;
  }
}

function parentIndex(index) {
  const pIndex = parseInt((index - 1)/2);

  if (pIndex >= 0)
    return pIndex;

  return null;
}

function swap(input, index1, index2) {
  const temp = input[index1];
  input[index1] = input[index2];
  input[index2] = temp;
}

function siftDown(arr, maxIndex) {
  let index = 0;
  let lIndex;

  do {
    lIndex = index*2 + 1;
    if (lIndex > maxIndex)
      break;
    // get largest child
    if (lIndex < maxIndex) {
      lIndex = arr[lIndex] > arr[lIndex+1] ? lIndex: lIndex + 1;
    }
    if (arr[index] >= arr[lIndex])
      break;
    swap(arr, index, lIndex);
    console.log(arr);
    index = lIndex;
    lIndex = index*2 + 1;
  } while (lIndex <= maxIndex);
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
