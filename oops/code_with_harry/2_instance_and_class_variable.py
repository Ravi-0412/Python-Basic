# variable created under 'constructor' are instance variable
# and variable created outside constructor just after class are class variable
# when we use 'self.variable_name' then it first seearch for instance variable
# if not present then only search for class variable
# we we write the 'class_name.variable_name' then it will first search for class variable


class Employee:
    increment= 1.5
    no_of_employee= 0
    def __init__(self,fname,lname,salary):
        self.fname= fname  # left side is instance variable and right side is the val passed by us
        self.lname= lname
        self.salary= salary
        self.increment= 3
        Employee.no_of_employee+= 1
    # to incr salary of employee
    def increase(self):
        self.salary= int(self.salary*Employee.increment)   # will check for class var 'increment' first
        # self.salary= self.salary*self.increment   # will incr acc to the instance variable
                                                    # will check for instance var first
print(Employee.no_of_employee)
harry= Employee('harry','jackson',44000)  # all objects will be created at diff add
rohan= Employee('rohan','gupta',44000)
print(Employee.no_of_employee)

print(harry.salary)
harry.increase()
# print("salary of harry after incr=")
print(harry.salary)  
print(harry.__dict__)   # will map the var with their values





