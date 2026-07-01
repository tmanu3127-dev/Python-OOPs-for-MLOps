# initiate a class

class employee:
    # special function of specil method or /magic/dunder method:
    def __init__(self):
        print("Started executing attributes/data ")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")


# When we used to call a function under a class we call that method:

    def travel(self,destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")        


# create an object/instance of the clas

sam = employee()



# print(sam.salary)

sam.travel ("Kerala")

        