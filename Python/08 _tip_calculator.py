#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill= float(input("What was the total bill? $ "))
tip = int(input("How much you want to give as tip? 10,12 or 15? "))
people= int(input("How many people you want to split?"))
bill_with_tip = (tip/100) *bill +bill
bill_per_person= bill_with_tip/people
final_amount= round(bill_per_person, 2)
print(f"each person should pay:$ {final_amount}")