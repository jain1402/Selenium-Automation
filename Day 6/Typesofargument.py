'''There are two types of Argument 
1. Positional Argument
2. Keyword Argument
'''
# def myfun(a,b):
#     print (a,b)

# myfun(10,20)  # This is positional Argument

def myfun(a=10,b=20): # This is Keyword Argument
    print(a,b)
    return(a+b)
sum = myfun()
print(sum)


def myfun(a,b=99): # This is Keyword Argument
    print(a,b)
    return(a+b)
sum = myfun(1)
print(sum)

def myfunct(a,b,c):
    print(a,b,c)

myfunct(10,20,30) #this positional Argument
myfunct(a=100,b=200,c=300) # This is Keyword Argument

# myfunct(1,b=2,3) # will give SyntaxError: positional argument always follows keyword argument