#finding size ofthe tuple
#1.using getsize() method
import sys
tuple1 = ['A',1, 'B', 2,'C', 3,'D',4]
tuple2 = ["manu", "yadhu", "leena", "diya"]
tuple3 = [("appu",1), ("malu",2), ("vinu", 3)]
print("Size of tuple1 :" + str(sys.getsizeof(tuple1))+"bytes")
print("Size of tuple2:" + str(sys.getsizeof(tuple2))+"bytes")
print("size of tuple3:" + str(sys.getsizeof(tuple3))+"bytes")
