class Employee:
    def __init__(self,fname,lname,salary):
        self.fname= fname  # left side is class variable and right side is the val passed by us
        self.lname= lname
        self.salary= salary

harry= Employee('harry','jackson','44000')  # all objects will be created at diff add
rohan= Employee('rohan','gupta','44000')

print(harry, rohan)  # will print add of objects 'rohan' and harry
print(harry.fname)
print(rohan.fname)
