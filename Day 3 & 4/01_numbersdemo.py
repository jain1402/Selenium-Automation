# creating a empty string

# name = ""
# name = ''

# Mutable  ( can change the value of variable )
# immutable ( can not change the value of variable )

# slicing of string

str = "welcome"
print(str[1:5])
print(str[0:3])
print(str[1:-1])



# ord () and chr() # Returns ASCII code and character
# # 
print (ord("A"))
print (chr(65))
print (chr(69))
print (ord("Z")) 

# in and not in operators # Returns Boolean Value

s= "welcome"

print ("come" in s)
print ("come" not in s)

# Testing Strings True/False

# s= 123
# print("s".isalnum())

s= "welcome to python"
print("s".isalpha())
print("welcome".isalpha())
print("123".isalnum())
print("2024".isdigit())
if (s.isalpha()):
    print (s)
else:
    print("No such thing exits ")

#  Searching for sub strings

s= "welcome  to python"

print(s.endswith("w"))
print(s.startswith("w"))
print(s.find("w"))
print(s.count("t"))
print(s.find("ayush")) # will Return -1 is element is not present

# converting string

s= "welcome TO Python"

s1= s.capitalize()
print(s1)

s2= s.lower()
print(s2)

s3= s.upper()
print(s3)

s4 = s.swapcase()
print (s4)

s5 = s.replace("ome", "ooo")
print(s5)


# print only even numbers between 1 to 10

print(list(range(0,10,2)))

# print only odd numbers between 1 to 10
print(list(range(1,10,2)))
