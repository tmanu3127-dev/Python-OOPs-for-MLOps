# Single or Basic Inheritance:

# Base Class:

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived Class:
# 
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# create an instance of the Child class

child = Child("Alice")
child.greet()  # Output: Hello, my name is Alice.
child.play()   # Output: Alice is playing.                  


# ----------------------------------------------------------------------

# Multilevel Inheritance:

class Grandparent:
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

# Intermediate Class:
# 
class Parent(Gradparent):
    def work(self):
        print(f"{self.name} is working.")

# Derived Class:
# 
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of the Child Class:
# 
child = Child("Charlie")
child.tell_stroy() #Output: Charlie tells a story.
child.work()      #Output: Charlie is working.
child.play()     #Output: Charlie is playing. 

#-------------------------------------------------------------------

# Hierachical Inheritance:

# Base Class:

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello,my name is {self.name}.")


# Derived Class 1:
# 
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")

# Derived Class 2:

class Child2(Parent):
    def study(self):
        print(f"{self.name} is studying.")

# Create instance of Child1 and Child2 classes:
# 
child1 = Child1("Dave")
child2 = Child2("Eve")

child1.greet() # Output: Hello, my name is Dave.
child1.play()  # Output: Dave is playing.

child2.greet() # Output: Hello, my name is Eve.
child2.study() # Output: Eve is studying.

# ----------------------------------------------------------------------

# Multiple Inheritance (Diamond Problem):

# Common Base Class 

class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from A, {self.name}.")

# Intermediate Class 1:
# 
class B(A):
    def greet(self):
        print(f"Hello from B, {self.name}.")
        super().greet()  # Call the greet method of class A

# Intermediate class 2:

class C(A):        
    def greet(self):
        print(f"Hello from C, {self.name}.")
        super().greet()  # Call the greet method of class A

# Derived Class:
#
class D(B, C):
    def greet(self):
        print(f"Hello from D, {self.name}.")
        super().greet() # Call the greet method of class B and C        


# Create an instance of D

d = D("Frank")
d.greet() # Output: Hello from D, Frank. Hello from B, Frank. Hello from C, Frank. Hello from A, Frank.



# ----------------------------------------------------------


# Hybrid Inheritance:

# Base Class

class Animal:
    def __init__(self, name):
        self.name = name


    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate Class 1 (Hierarchical inheritance)

class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate Class 2 (Multiple Inheritance)

class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived Class (Multiple Inheritance)

class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name) # Explicitly calling the conductor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# create an instance of Bat
# 
bat = Bat("Bruce")
bat.sound() # output:Bruce makes a sound
bat.feed() # output: bruce is feeding milk.
bat.fly()  # output: Bruce is flying.
bat.nocturnal() # Output: Bruce is nocturnalsss                                        


