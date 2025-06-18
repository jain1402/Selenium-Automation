''' A tuple is a collection which is ordered and unchangeable
 A Tuple is IMMutable , In python tuple is written as using round bracket ()
 1. we cannot insert a new value in a tuple.
 2. we can not append a new value
 3. we cannot modify a existing value
 4. we cannot remove a value 
 '''

'''mytuple=("A","b","c","d","e","f","G")
print(mytuple)
print(mytuple[1])
print(mytuple[0:1])
print(mytuple[0:-1])
print(mytuple[1-2:4-1])'''


#  changing the items of a tuple
#  tuple ---> list --> modify --> tuple

mytuple= ("ramesh", "suresh", 100 , 200 , "nobody")
mylist=list(mytuple)
mylist[0]= "Ayush"

mytuple=tuple(mylist)

print(mytuple)

# Print each item of tuple

mytuple= ("ramesh", " suresh", 100 , 200 , "nobody")

for i in mytuple:
    print(i)