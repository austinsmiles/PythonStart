# ---- List operations start -----

varList1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  # Initialize a list with square brackets []
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
varList1.append("12")
varList1.append(newelement)
print("Adding some elements", newelement, ". New list is : ", varList1)
varList1.remove(newelement)  # Removes first occurrence of 11
print("Removing ", newelement, ". New list is : ", varList1)
del varList1[len(varList1) - 1]  # same as varList1.pop()
print(varList1)
varList2 = varList1.copy()  # same as varList2=list(varList1)
print("Copied list : ", varList2)
varList3 = varList1 + varList2  # same as varList1.extend(varList2)
print("Joined list 3 : ", varList3)
del varList3  # deletes the list
# ---- List operations end -----

# ---- Tuple operations start -----
# Most operations for list are valid for tuple, except add/append and remove/del items
varTuple1 = ("apple", "banana", "cherry")  # Initialize a tuple with round brackets ()
print("Tuple before change", varTuple1)  # ('apple', 'banana', 'cherry')
varListTuple1 = list(varTuple1)
varListTuple1[1] = "kiwi"
varTuple1 = tuple(varListTuple1)
print("Tuple after change", varTuple1)  # ('apple', 'kiwi', 'cherry')

varSingleValidTuple = ("apple",)
print(type(varSingleValidTuple))  # <class 'tuple'>

# NOT a tuple
varSingleInvalidTuple = ("apple")  # comma missing at the end, so the tuple is invalid
print(type(varSingleInvalidTuple))  # <class 'str'>
# ---- Tuple operations end -----

# ---- Set operations start -----
varSet1 = {"apple", "banana", "cherry"}  # Initialize a set with curly brackets {}
print("Original set :", varSet1)
varSet1.update(["orange", "mango", "grapes"])
print("Updated set : ", varSet1)
removeSetElement = "grapes"
varSet1.remove(removeSetElement)
"""same as discard()
only difference is discard() will not 
throw error if element is not present"""
print("Removed ", removeSetElement, " from set : ", varSet1)
varSet1.pop()
print("Popped from set. Remaining elements:",
      varSet1)  # Not recommended since set is unordered and last element is unknown
varSet2 = {"NewYork", "Washington", "Chicago"}
varSet3 = varSet1.union(varSet2)  # same as varSet1.update(varSet2). Both will exclude duplicates
print("Union set 1 and 2 :", varSet3)
# ---- Set operations end -----

# ---- Dictionary operations start -----
varDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Keys : ", end="")
for k in varDict:
    print(k, end="|")  # Print keys
print()
print("Values : ", end="")
for v in varDict:  # can also use varDict.values() to iterate through values
    print(varDict[v], end="|")  # Print values
print()
for k, v in varDict.items():
    print(k, ":", v, end="|")
print()
dictPopElement = "brand"
varDict.pop(dictPopElement)
print("Popped ", dictPopElement, " from dict. Remaining : ", varDict)
varDict.popitem()
print("Popped item from dict. Remaining : ", varDict)

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for c, cv in myfamily.items():
    print(cv["name"])  # get the name of all nested dictionaries
# ---- Dictionary operations end -----

# ---- Iterator operations start -----
cities = ("New York", "San Francisco", "Chicago")
citiesIterator = iter(cities)
for x in citiesIterator:
    print(x, end=",")
# ---- Iterator operations end -----
