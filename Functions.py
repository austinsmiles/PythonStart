import MyModule as mm  # alias for MyModule


# from MyModule import Person --> use this to import something specific from the module

# Functions
def my_function(arg):
    global name
    name = arg
    print("Hello ", arg)


my_function("Sarah")
print("Global variable name is :", name)  # Accessing the global variable here, set as Sarah in 1st call

my_function("Connor")
print("Global variable name is :", name)  # Accessing the global variable here, set as Connor in 2nd call


def my_function(*kids):  # Tuple of args (arbitrary args)
    print("Arbitrary arg kids[2] : " + kids[2])


my_function("Steve", "Sarah", "Elaine")


def my_function(child3, child2, child1):  # keyword args, order doesnt matter
    print("Keyword args child3 : " + child3)


my_function(child1="Steve", child2="Sarah", child3="Elaine")


def my_function(**kid):  # Dictionary of args (arb keyword args --> kwargs)
    print("His last name is " + kid["lname"])


def my_function(country="The Future"):
    print("I am from " + country)


my_function("New York")  # Override default param with Canada
my_function()  # Take the default parameter here

lambdaFn = lambda a: a + 10
print(lambdaFn(5))  # Pass 5 to the lambda fn, return 5+10 = 15


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

mm.myModuleGreeetMethod("The Terminator")
print("I am back for ", mm.target["name"])

# Built-in modules
import platform

varSys = platform.system()
print(varSys)
varDir = dir(platform)
print(varDir)

# Working with JSON
import json

# some JSON:
inJsonStr = '{ "name":"John Connor", "age":16, "city":"New York"}'

# parse x:
jsonObj = json.loads(inJsonStr)

# the result is a Python dictionary:
print(jsonObj["name"])

jsonStr = json.dumps(jsonObj, indent=2)  # use separators=(". ", " = ") for json customization

print("JSON string is ", jsonStr)

# Working with Regex
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

x = re.findall("ai", txt)
print(x)

x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

x = re.split("\s", txt)
print(x)

# You will need --> pip install camelcase
import camelcase

c = camelcase.CamelCase()

txt = "hello world is in lowercase"

print(c.hump(txt))

# Try except
try:
  print(undefinedVariable)
except NameError:
  print("Variable is not defined")
except:
    print("Something else went wrong")
finally:
    print("End credits roll")


#String formatting
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price)) # Substitute price 49 in curly braces

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price)) # Using multiple values

uantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price)) # Using index numbers

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name)) # You can use same index multiple times

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang")) # Named indexes

#File handling
f = open("demofile.txt", "r")
print(f.read())

import os
#os.remove("demofile1.txt") This will remove the file