#  Conditional statement
# 1. if , if - else , elif 

#  Example 1 : print a person is eligible for voting or not
#    age>=18

age = int(input("Enter the Age of the person:"))

if(age >= 18):
    print ( "you are eligible for voting")
else:
    print ("you are not eligible for vote")   


# Example 02 : finding a number is even or odd

num = int(input("Enter the number:"))

if(num%2==0):
    print ( "it is an even number")
else:
    print ("it is an odd number")

# # Multiple condition usinf elif

# num = int(input("Enter the number:"))

if num==0:
    print ( "it is sunday")
elif (num==1):
    print("its Monday")
elif (num==2):
    print("its tuesday")
elif (num==3):
    print("its wednesday")
elif (num==4):
    print("its thursday")
elif (num==5):
    print("its friday")
elif (num==6):
    print("its saturday")
else:
    print("out of range") 

#  Check largest of 3 numbers

num1 = int(input("Enter 1st no:"))
num2 = int(input("Enter 2nd no:"))
num3 = int(input("Enter 3rd no:"))

greatest_no = max(num1,num2,num3)

print(f"the maximum of three is : {greatest_no}")

# def find_greatest_of_three_numbers (num1 , num2, num3):
#     greatest = max(num1,num2,num3)
#     return greatest
# print("Enter Three Numbers")
# try:
#     num1 = float(input("Enter no. 1 :- "))
#     num2 = float(input("Enter no. 2:- "))
#     num3 = float(input("Enter no. 3:- "))
    
#     greatest = find_greatest_of_three_numbers(num1,num2,num3)
#     print(f"the greatest of three no. is : {greatest}")
# except(ValueError):
#     print("please enter valid numbers")