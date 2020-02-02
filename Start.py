import random

# comment text
"""
Basic beginner tutorial program for Python 3.7
Created by Austin Perez
This is how to write a multi line comment
"""

var1 = "John"  # Declare with double quote
var2 = 'Adam'  # Declare with single quote
print("Hello World!")

# data types -- start --

varStr = "Hello World"
varIntx = 20
varFloatx = 20.5
varComplex = 1j
varList = ["apple", "banana", "cherry"]
varTuple = ("apple", "banana", "cherry")
varRange = range(6)
varDict = {"name": "John", "age": 36}
varSet = {"apple", "banana", "cherry"}
varFrozenSet = frozenset({"apple", "banana", "cherry"})
varBool = True
varBytes = b"Hello"
varByteArray = bytearray(5)
varMemoryView = memoryview(bytes(5))

# data types -- end --

x = 1  # int
y = 2.8  # float
z = 1j  # complex

print("float form of ", x, " is ", float(x))  # 1.0
print("int form of ", y, " is ", int(y))  # 2
print("complex form of ", x, "is", complex(x))  # 1+0j

print(random.randrange(1, 10))  # prints a random number between 1-10. import random module for this

varMultilineStr = """Assigning a
milti line string to a 
variable"""
print(varMultilineStr)
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True

# Conditions
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

a = 2
b = 330
print("A") if a > b else print("B")  # short hand if-else

i = 1
while i < 6:
    print(i,end=",")
    i += 1
else:
    print("i is no longer less than 6")

for i in range(6):  # 0-5, increment 1
    print(i,end=",")
print()
for i in range(2,20,3):  # 0-19, increment 3
    print(i,end=",")
else:
    print("Finally finished!")

