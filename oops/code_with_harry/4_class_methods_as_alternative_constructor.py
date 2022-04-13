# class methods as an alternative constructors
# just pass the variable in a string
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
    @classmethod
    # def from_str(cls,emp_string):
    #     fname, lname, salary= emp_string.split("-")  # if you are passing the string separated by "-"
    #                                                  # then use "-" i.e use the same symbol by which 
    #                                                  # you are passing the all the variables(separated by)
    #     return cls(fname,lname,salary)

    @classmethod
    def from_str(cls,fname,lname,salary):
        return cls(fname,lname,salary)

# harry= Employee('harry','jackson',40000)  # all objects will be created at diff add
# rohan= Employee('rohan','gupta',50000)

harry= Employee.from_str('harry','jackson','40000')   # even you are writing this you will have
                                                     # to write the constructor with same no of arguments
                                                     # your class methods variables can be diff than constructo
rohan= Employee.from_str('rohan','gupta','50000')
print(harry.fname)
print(rohan.fname)
