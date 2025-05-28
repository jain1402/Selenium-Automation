'''Four type of collection supported in python
    1. List
    2. Tuple
    3. Set
    4. Dictionary
'''


''' A list is a collection which is ordered and changeable
 A list is Mutable , In python list is written as using square bracket []
 '''


# mylist1 = [ 10 , 20 , 30 ,45 ,50]
# mylist2 = ["ayush","jain"]
# mylist3 = list()  # Empty list
# print( mylist1)
# print( mylist2)

# print( mylist1[-1]) # Print last value from the list
# print( mylist1[-2]) # print 2nd last value from the list


''' 1. Print all items in the list
    2. check particular item present in the list
    3. Insert Item in the list
'''
# mylist = [ "Amit", "ramesh" , "suresh" ,"rajesh" ,"nobody"]

# # Example 1

# for i in mylist:
#     print (i)
# # Example 2

# if "ramesh" in mylist:
#     print("yes . Ramesh is there")
# else:
#     print ("No such item is present")

# #  For insert any item we use append() and Insert() method


# mylist = [ "Amit", "ramesh" , "suresh" ,"rajesh" ,"nobody"]

# mylist.append("Ayush")
# print(mylist)

# mylist.insert(0 , "Ayush")
# print(mylist)

# # Delete or Remove items from th list

# #  Examle 1 ( POP function)

# mylist = [ "Amit", "ramesh" , "suresh" ,"rajesh" ,"nobody"]

# mylist.pop(4)
# print(mylist)

# #  Examle  (del)
# del mylist[3]
# print(mylist)

# # copy a list
# mylist = [ "Amit", "ramesh" , "suresh" ,"rajesh" ,"nobody"]
# mylistnew=list(mylist)
# print(mylistnew)

#  Joining of the list
mylist1 = [ "Amit", "ramesh" , "suresh" ,"rajesh" ,"nobody"]  # Approach 1

mylist2 = [ 10 , 20 , 30 ,45 ,50]

# mylist3= mylist1 + mylist2
# print(mylist3)

#  Approach 2 using looping statement

for i in mylist2:
    mylist1.append(i)
print(mylist1)

mylist1.extend(mylist2)
print(mylist1)
