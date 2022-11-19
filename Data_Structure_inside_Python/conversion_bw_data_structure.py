# to convert any data type to 'string' in proper string format
# just use: ''.join(name_of_data_type) , whatever we will write 
# inside the '' , ele will get joined by that char 
# but join can't be same as the given order, it can join into any order

s = {'a', 'b', 'c', 'd'}  # it is a set not dictionary
print(type(s))
print(s)  # can print in any order
print(' '.join(s))   # you can store in variable also then print
print(''.join(s))


# to convert any data types to other one
# just write the variable name inside the types in which you want to convert
s1= "geeksforgeeks"
print(list(s1))

# for converting list into string use the first two method
a= [1,2]
print("".join(str(e) for e in a))

a= ['1','2']
print("".join(a))

a= [1,2]   
print("".join(str(a)))   # this will return the same list

# even writing like this will return the same list. Don't know why 
a= [1,2]
b= str(a)    # showing type 'str' only but printing the same list only
print("".join(str(b)))


# note: using join you can store in any other data structure iff they are converted first to char like:
a= [1,2]
print("".join(str(e) for e in a))
# e.g: 
a= [1,2]
b= []
b.append("->".join(str(e) for e in a))
print(b)   # will print ['1->2']   # will join each ele in list by "->"

# but this will print totally different
a= [1,2]
b= []
b+= "->".join(str(e) for e in a)   
print(b)    # ['1', '-', '>', '2']   # just cosidered all the char in above print as char 




