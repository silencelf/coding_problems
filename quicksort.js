function quickSort(input, low, high) {
  if (low < high) {
    const pi = partition(input, low, high);
    quickSort(input, low, pi - 1);
    quickSort(input, pi + 1, high);
  }
}

function partition(arr, low, high) {
  const pivot = arr[high];
  let i = low - 1;
  for (let j = low; j < high; j++) {
    if (arr[j] < pivot) {
      i++;
      let tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
  }
  let tmp = arr[i + 1];
  arr[i + 1] = arr[high];
  arr[high] = tmp;

  return i + 1;
}

let input = [3, 1, 23, 2, 235, 88, 634, 27, 73, 56, 89, 14, 22];
quickSort(input, 0, input.length - 1);
console.log(`sorted array: ${input}`);

input = [1, 2, 3, 4, 5];
quickSort(input, 0, input.length - 1);
console.log(`sorted array: ${input}`);
