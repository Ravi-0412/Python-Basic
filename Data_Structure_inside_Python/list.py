# https://www.geeksforgeeks.org/difference-between-list-and-array-in-python/
# https://stackoverflow.com/questions/27073596/what-is-the-cost-complexity-of-insert-in-list-at-some-location

# lst=['one','two','three','four']
# lst1= [1,2,'ram']
# lst.append('five')

# lst.insert(2,'nine') # insert at specific location
# print(lst)

# lst.remove('two')   # will remove two from the list

# lst.append(lst1)  # will append the list1(in list form itself) at the last of lst
# print(lst)
# lst.extend(lst1)  # will only append elements of lst(not with list form) in the lst
# print(lst)

# del lst[1]   # will delete the ele at index '1' from the list
# print(lst)
# a= lst.pop(1)  # will delete the ele at index '1' from the list
# print(a)
# print(lst)


# lst=['one','two','three','four',1,2,3]
# if 'two' in lst:
#     print('hii')
# if 'six' not in lst:
#     print('hello')


# numbers= [3,1,6,2,8]
# numbers.sort()   # will sort the list in the given list itself(in place sorting)
                  # used when we don't need the original list
                  # this method 'sort' is only defined for list
# sorted(numbers)  # it returns a new sorted list ,so to get the sorted list you have to
                   # store the result in another list
                   # original list will be same as before only
# sorted_lst= sorted(numbers)  # this method 'sorted' accepts any iterable like string,set,tuple etc..
# print("sorted list: ", sorted_lst)
# print("original list: ", numbers)
# print("reverse ordered list: ", sorted(numbers,reverse=True))  # will sort  the list in the des order


# s="my name is Ravi Raushan"
# split_lst= s.split()  # return a list with words of string as elements
# print(split_lst)


# numbers= [10,20,30,0,50,60,70,80]
# print(numbers[:])
# print(numbers[0:4])
# print(numbers[::2])
# print(numbers[2::2])


# method 1: adding two list
# list1= [10,20,30,0,50,60,70,80,10,10]
# list2=[1,2,3,4]
# new_list= list1 + list2
# print(new_list)
#  print(list1.count(10))   # will count the no of '10' in the given list

# method2 : to add list
# using extend() function
'''
The Python’s List extend() method iterates over an iterable like string, 
list, tuple, etc., and adds each element of the iterable to the end of List.
The length of the list increases by the number of elements present in the iterable.
Syntax: list.extend(iterable)

Parameters:

iterable: Any iterable (list, set, tuple, etc.)
Returns:

The extend() method modifies the original list. It doesn’t return any value.
'''
my_list = ['geeks', 'for']  
# Another list
another_list = [6, 0, 4, 1] 
# Using extend() method
my_list.extend(another_list)
print(my_list)

# e.g: 2
my_list = ['geeks', 'for', 'geeks']
my_tuple = ('DSA', 'Java')
my_set = {'Flutter', 'Android'} 
# Append tuple to the list
my_list.extend(my_tuple)  
print(my_list)  
# Append set to the list
my_list.extend(my_set)
print(my_list)

# e.g: 3
# my_list = ['geeks', 'for', 6, 0, 4, 1]  
# my_list.extend('geeks') # will add whole string(single letters wise) to the end of the list
# print my_list
# output: ['geeks', 'for', 6, 0, 4, 1, 'g', 'e', 'e', 'k', 's']


# reversing a list in python

# method 1: using list.reverse()    # this method will return the object. for printing store in list
# if you will print(list.reverse), it will print None. same for other inbuilt method, you have to print in separate line after using the function
# method 2: using a= reversed(list)  # like this

# method 3: list1= list[::-1]

# for reversing in the specific range , by using slicing
# for slicing nums[a:b:c], always remember that 'a': represents starting index, 'b': represents the end index excluding the end index 
# and 'c': represents the steps to move and if 'c' is negative means we have to move in opposite direction with given move from start index to end index(excluding) 
# and if 'a',or  'b' is not given then we have to move in whole array either in positive direction or opposite direction depending upon the sign of 'c'
nums= [1,2,3,4,5,6,7]
n= len(nums)
k=3
# nums1= nums[k:-1:-1]  # for reversing like this till index 0(in opposite direction) it wont work, don't know why 
# so use 
# nums1= nums[k::-1]   # will reverse the array from index k to index 0 (minimum possible index)
# part = nums[4:1:-1] # will reverse from index '4' to '2'(before 1)
# print(part)
# print(nums1)


# square= []
# for i in range(10):
#     square.append(i**2)
# print(square)


# square=[i**2 for i in range(10)]
# print(square)


# list2=[1,2,3,4]
# new_list=[i*2 for i in list2]
# print(new_list)


# numbers= [10,20,-30,0,-50,60,70,80]
# new_list= [i for i in numbers if i>=0]
# print(new_list)


# new_list= [(i,i**2) for i in numbers]
# print(new_list)


# iterating for num directly in list for specific range
arr = [17,18,5,4,6,1]
n= len(arr)
k=1
for num in arr[k:4]:  # in this only num iterate, index always remains same
                      # for operation related with index, you have to 
                      # increment index separately
    print(num)
    #k+= 1
print(k)  # will print 1 only


# for finding maximum, minimm etc for a specific range in any data supported data structure of python
arr = [4,9,8,4,7,10,1,15]
n= len(arr)
k=max(arr[2:])
j= max(arr[4:7])
p= max(arr[1:5])
r= max(arr[5:7])
print(k)
print(j)
print(p)
print(r)


# deleting a list or some elements of a list

# a= [1,2,3,4,5,6,7,8]
# del a[:]  # will delete whole list
# print(a)

a= [1,2,3,4,5,6,7,8]
# del a[2:]  # will delete everything from index 2
del a[2:-2]  # will delete everything from index 2 
            # to last two ele(won't delete last two ele)
print(a)

# a.clear()     # will delete whole list
# a= []      # another way to delete all ele



# inserting an ele at specific index in python
# https://www.geeksforgeeks.org/python-list-insert/
a= [1,2,3]
# a.insert(index, ele)
# after inserting that ele at proper index, it will just move all the ele after that index one step ahead
# it doesnt delete the index at that position


a=[]*n  # this will not allocate the space for n ele, space will only be allocated when we will initialise the array with some element
a= []*6
a.insert(2,3)
a.insert(4, 4)
print(a)
# when you will do "insert operation at a fixed index" on this(empty or uninitialised array) 
# it will start inserting from start only not from the given index.

# as list is dynamic, it doesn't create the memory for n ele at the start itself.
# this will happen for all type of data structure in python if you will try any operation on empty and uninitialised data structure.
# so better initialise with some proper value and then do the operation then, all operation will work normally.



# adding two lists
print([]+[1])          # output: [1]
print([[]]+ [[1]])     # output: [[], [1]]

# appending in 2d and 1d array
# append basically means add the new ele after all the existing ele 
a= [[]]   
a.append([3])   # for this 2D array existing ele is '[]'
print(a)     # will print [[], [3]]


a= []
a.append(3)   # here there is no existing ele
print(a)    # will print '[3]'



# both will print the different thing
# https://stackoverflow.com/questions/16641119/why-does-append-always-return-none-in-python
a= []
print(a.append(4))   # giving 'None' as output. Actually 'append' is a type of void function 
                    # and after appending it's returning according to the 'append' function.
                    # basically printing the returned value of append which is always 'None'

# in this we are printing the list 
a= []
a.append(4)
print(a)     


# unusual way python work(shocked)
# i was thinking when we will print the value of 'i' outside the function then it will be '4'(value passed inside range)
# but it stops at max possible value only
# came through this in Q : "199. Binary Tree Right Side View"
for i in range(4):
    print(i,"in")
print(i)   # will print '3' only
