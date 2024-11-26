# finding k th smallest and largest element in tuple
#1. using heapq mathod
import heapq
mytuple = [10, 20, 350, 400, 15]
k = 3
smallest_k = heapq.nsmallest(k, mytuple)
largest_k = heapq.nlargest(k, mytuple)
print(f"{k} smallest element:{smallest_k}")
print(f"{k} largest element: {largest_k}")
