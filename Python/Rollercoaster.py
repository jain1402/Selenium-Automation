print("Welcome to the rollercoater ride")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What is you age? "))
  if age < 12:
    print("You have to pay 5$ ")
  elif age < 18:
    print("You have to pay 7$ ")
  elif age > 18:
    print("You have to pay 12$ ")
else :
  print("You cannot ride the rollercoaster")