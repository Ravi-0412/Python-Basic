# we use class methods when we want to update the class variable
# also when we don't want to pass object as an argument
# it takes class as argument and increases the respective class variable
class Employee:
    increment= 1.5
    def __init__(self,fname,lname,salary):
        self.fname= fname  # left side is instance variable and right side is the val passed by us
        self.lname= lname
        self.salary= salary
        self.increment= 3
    # to incr salary of employee
    def increase(self):
        self.salary= int(self.salary*Employee.increment)   # will check for class var 'increment' first
        # self.salary= self.salary*self.increment   # will incr acc to the instance variable
                                                    # will check for instance var first
    @classmethod  # before class method you have to write like this
    def change_increment(cls,amount):  # 1st one is class as var like self for instance
                                       # 2nd para is the value by which you want to incr the class var
        cls.increment= amount  # will incre the class var 'increment' by the given amount
                               # same way we write for instance var i.e: 'self.var='        


harry= Employee('harry','jackson',40000)  # all objects will be created at diff add
rohan= Employee('rohan','gupta',50000)

print(harry.salary)
Employee.change_increment(4)  # we call the class methods like this
# print("salary of harry after incr=")
harry.increase()
print(harry.salary)  