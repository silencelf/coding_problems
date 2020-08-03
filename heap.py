#! /usr/bin/python3

class Heap:
    arr = []
    loc = {}

    def __init__(self, arr):
        self.arr = arr
        self.__buildHeap__(arr)
    
    def __str__(self):
        return str(self.arr)

    def extract(self):
        if not self.arr:
            return None
        val = self.arr[0]
        self.loc[self.arr[-1][1]] = 0
        del self.loc[self.arr[0][1]]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.__heapify__(self.arr, len(self.arr), 0)
        return val

    def peek(self):
        if self.arr:
            return self.arr[0]
        return None

    def add(self, key, value):
        self.arr.append((key, value))
        self.loc[value] = len(self.arr) - 1
        index = len(self.arr) // 2
        while True:
            self.__heapify__(self.arr, len(self.arr), index)
            if index == 0:
                break
            index = (index - 1) // 2

    def __heapify__(self, arr, n, i):
        smallest = i
        l = i*2 + 1
        r = i*2 + 2
        if l < n and arr[l][0] < arr[smallest][0]:
            smallest = l
        if r < n and arr[r][0] < arr[smallest][0]:
            smallest = r
        if i != smallest:
            self.loc[arr[i][1]] = smallest
            self.loc[arr[smallest][1]] = i
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.__heapify__(arr, n, smallest)

    def __buildHeap__(self, arr):
        self.loc = { arr[i][1] : i for i in range(len(arr)) }
        startIndex = len(arr) // 2 - 1
        for i in range(startIndex, -1, -1):
            self.__heapify__(arr, len(arr), i)

input = [(17, 'a'), (15, 'b'), (13, 'c'), (9, 'd'), (6, 'e'), (5, 'f'), (10,
    'g'), (4, 'h'), (8, 'i'), (3, 'j'), (1, 'k')]
heap = Heap(input)
print(heap)
print(heap.loc)

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
val = heap.add(1, 'k')
print(heap)
print(heap.loc)
val = heap.add(3, 'j')
print(heap)
print(heap.loc)
val = heap.add(4, 'h')
print(heap)
print(heap.loc)
val = heap.add(5, 'f')
print(heap)
print(heap.loc)
val = heap.add(6, 'e')
print(heap)
print(heap.loc)

heap = Heap([])
print(heap)
print(heap.loc)
heap.add(5, 'A')
print(heap)
print(heap.loc)
heap.add(3, 'B')
print(heap)
print(heap.loc)
heap.add(1, 'C')
print(heap)
print(heap.loc)
