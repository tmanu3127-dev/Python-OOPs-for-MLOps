# Simple Inhertiance:

## Base Class

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")


## Derieved Class:

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")


# Create an instance of the Animal Class
# 
animal = Animal("Generic Animal")
animal.speak() # output: generic animal makes a sound.

## Create an instance of the Dog Class

dog = Dog("Buddy")
dog.speak() # output: Buddy barks.



# Super Keyword:It is used only inside the child class to refer to the parent class. It is used to call the parent class methods and constructors. It is used to avoid overriding the methods of the base class in the derived class.

# Super keyword is used to call the parent class methods from the child class. It is used to access the methods of the base class from the derived class. It is used to avoid overriding the methods of the base class in the derived class.

# Base Class:

class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        print(f"{self.name} makes a sound.")

## Derieved Class:

class Dog(Animal):
    def __init__(self,breed):
        super().__init__() # calling the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()# calling the parent/base class method 
        print(f"{self.name} barks. It is a {self.breed}.")   


## Create an instance of the Dog Classs


dog = Dog("Golden Retriever")
dog.speak() # output: Buddy makes a sound. Buddy barks. It is a Golden Retriever.
