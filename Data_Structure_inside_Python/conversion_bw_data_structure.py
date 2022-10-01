# to convert any data type to 'string' in proper string format
# just use: ''.join(name_of_data_type) , whatever we will write 
# inside the '' , ele will get joined by that char 
# but join can't be same as the given order, it can join into any order

s = {'a', 'b', 'c', 'd'}
print(s)
print(' '.join(s))   # you can store in variable also then print
print(''.join(s))


# to convert any data types to other one
# just write the variable name inside the types in which you want to convert
s1= "geeksforgeeks"
print(list(s1))



