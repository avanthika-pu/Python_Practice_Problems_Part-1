#finding smallest and largest k element from tuple
# using sort method
mytuple = (10, 50, 20, 15, 45, 100, 150, 240, 5)
k=3
smallest_k = sorted(mytuple)[:k]
largest_k = sorted(mytuple, reverse = True)[:k]
print(f"{k} smallest element:{smallest_k}")
print(f"{k} largest element:{largest_k}")
