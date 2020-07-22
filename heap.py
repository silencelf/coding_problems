#! /usr/bin/python3

class Heap:
    arr = []

    def __init__(self, arr):
        self.arr = arr
        self.__buildHeap__(arr)
    
    def __str__(self):
        return str(self.arr)

    def extract(self):
        if not self.arr:
            return None
        val = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.__heapify__(self.arr, len(self.arr), 0)
        return val

    def peek(self):
        if self.arr:
            return self.arr[0]
        return None

    def add(self, value):
        self.arr.append(value)
        index = (len(self.arr) - 2) // 2
        while True:
            self.__heapify__(self.arr, len(self.arr), index)
            if index == 0:
                break
            index = (index - 1) // 2

    def __heapify__(self, arr, n, i):
        smallest = i
        l = i*2 + 1
        r = i*2 + 2
        if l < n and arr[l] < arr[smallest]:
            smallest = l
        if r < n and arr[r] < arr[smallest]:
            smallest = r
        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.__heapify__(arr, n, smallest)

    def __buildHeap__(self, arr):
        startIndex = len(arr)//2 - 1
        for i in range(startIndex, -1, -1):
            self.__heapify__(input, len(input), i)

input = [17, 15, 13, 9, 6, 5, 10, 4, 8, 3, 1]
heap = Heap(input)
print(heap)
print(heap.peek())

# extract elements
print('extract:')
val = heap.extract()
print(val)
print(heap)
val = heap.extract()
print(val)
print(heap)
val = heap.extract()
print(val)
print(heap)
val = heap.extract()
print(val)
print(heap)
val = heap.extract()
print(val)
print(heap)

# add more elements
print('add:')
val = heap.add(1)
print(heap)
val = heap.add(3)
print(heap)
val = heap.add(4)
print(heap)
val = heap.add(5)
print(heap)
val = heap.add(6)
print(heap)
