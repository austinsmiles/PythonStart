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

# ---- List operations start -----

varList1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print("List first: ", varList1[0])  # 1
print("List last : ", varList1[-1])  # 10
print("List fwd range:", varList1[2:5])  # ['3', '4', '5'] -- includes lower index(2), excludes upper index(5)
print("List rev range:", varList1[-5:-2])  # ['6', '7', '8'] -- includes lower index(-2), excludes upper index(-5)
print("Printing the array:")
for x in varList1:
    print(x, end="|")
print()
chk = "3"
if chk in varList1:
    print(chk, " is present in the array ", varList1)
print("Length of the array is ", len(varList1))  # 10

newelement = "11"
varList1.append(newelement)
print("Adding ", newelement, ". New list is : ", varList1)
varList1.remove(newelement)
print("Removing ", newelement, ". New list is : ", varList1)
del varList1[len(varList1) - 1]  # same as varList1.pop()
print(varList1)
varList2 = varList1.copy()  # same as varList2=list(varList1)
print("Copied list : ", varList2)
varList3 = varList1 + varList2  # same as varList1.extend(varList2)
print("Joined list 3 : ", varList3)
del varList3 #deletes the list
# ---- List operations end -----

# ---- Tuple operations start -----
# Most operations for list are valid for tuple, except add/append and remove/del items
varTuple1 = ("apple", "banana", "cherry")
print("Tuple before change", varTuple1)
varListTuple1 = list(varTuple1)
varListTuple1[1] = "kiwi"
varTuple1 = tuple(varListTuple1)
print("Tuple after change", varTuple1)

varSingleValidTuple = ("apple",)
print(type(varSingleValidTuple))  # <class 'tuple'>

# NOT a tuple
varSingleInvalidTuple = ("apple")  # comma missing at the end, so the tuple is invalid
print(type(varSingleInvalidTuple))  # <class 'str'>
# ---- Tuple operations end -----
