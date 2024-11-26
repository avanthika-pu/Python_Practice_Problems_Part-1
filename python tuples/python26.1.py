#finding size of tuple
#2. using __sizeof__ method
tuple1 = ["manu", "appu", "maya"]
tuple2 = [1,'A',2,'B',3,'C',4]
tuple3 = [(1,"manu"), (2,"appu"), (3,"malu")]
print("size of tuple1:" +str(tuple1.__sizeof__()) + "bytes")
print("size of tuple2:" +str(tuple2.__sizeof__()) + "bytes")
print("size of tuple3:" +str(tuple3.__sizeof__()) + "bytes")