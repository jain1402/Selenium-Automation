# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

stateOne = ["L", "O", "V", "E"]
stateTwo = ["T", "R", "U", "E"]

stateOneCount = 0
stateTwoCount = 0

name = name1 + name2

for i in name:
    if stateOne.__contains__(i.upper()):
        stateOneCount += 1
    elif stateTwo.__contains__(i.upper()):
        stateTwoCount += 1

print(stateOneCount)
print(stateTwoCount)