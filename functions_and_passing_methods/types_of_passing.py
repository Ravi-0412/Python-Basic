def update(x):
    print(id(x))  # will have same address as 'a' before update
    x= 8
    print(id(x))  # now will have diff address as 'a' after update
    print("x= ",x)

a= 10
print(id(a))
update(a)
print(id(a))
print("a= ",a)  # will not change as int varibale is mutable
# Int variables are immutable. So when an integer type is assigned to a new variable, 
# it should create a new object, right? But it only creates a new object when changes are made to either variables

# will print x= 8 and a= 10 value of 'a' will not change 
# when you call a function by passing a variable value,
# it is passed by value not by reference . but when 
# you will change the val of formal para, it will change the add of formal parameter not actual para



def update(lst):
    print(id(lst))  # will have same address as 'a' before update
    lst[1]= 25
    print(id(lst))  # now will have diff address as 'a' after update
    print("updated lst= ",lst)

lst = [10,20,30]
print(id(lst))
update(lst)
print(id(lst))
print("lst: ", lst)

# will update the original list also at same address since list is mutable 
# in earlier cases it was not changing because that variable
# 'a' was type of int which is immutable


