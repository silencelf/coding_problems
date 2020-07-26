#! /user/bin/python3

from queue import PriorityQueue

customers = PriorityQueue()

customers.put(2, "Harry")
customers.put(3, "Charles")
customers.put(1, "Riya")
customers.put(4, "Stacy")

while customers:
    print('-'*20)
    print(customers.get())
