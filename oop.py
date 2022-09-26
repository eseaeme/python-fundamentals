# Object Oriented Programming
"""Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods.

"""

## https://www.w3schools.com/python/python_classes.asp
## https://www.w3schools.com/python/python_inheritance.asp
## https://www.programiz.com/python-programming/object-oriented-programming
class Item:
    """__init__ function: 
    Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    """
    def __init__():

    """Objects Methods: Methods in objects are functions that belong to the object.
    They are used to define the behaviors of an object.
    """
    def calculate_total_price(self, x, y):
        return x * y


    """pass Statement: class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error."""
    
    def pass_method(self):
        pass # This is it. Then when calling this method there will be a pass.

item1 = Item()
item1.calculate_total_price()


## Encapsulation


## Polymorphism
"""Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
"""

## Inheritance
"""
Inheritance is a way of creating a new class for using details of an existing class without modifying it. 
The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).
Different types of Inheritance:
- Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
- Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.
- Multilevel inheritance: When we have a child and grandchild relationship. 
"""

"""Single Inheritance"""
class Person(object): # parent class
	def __init__(self, name, idnumber):	# __init__ is known as the constructor
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

class Employee(Person): # child class
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

"""Multiple Inheritance"""
class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")

class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")

class Derived(Base1, Base2):
	def __init__(self):
		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")

	def printStrs(self):
		print(self.str1, self.str2)

ob = Derived()
ob.printStrs()
