bill=0
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm?"))
if height >= 120:
        print("You can ride the rollercoster! ")
        age = int(input("What is your age? "))
        if age < 12:
            bill = 5
            print(f"You have to pay ${bill}.")
        elif age <= 18:
            bill = 7
            print(f"You have to pay ${bill}.")
        elif age >= 45 and age <= 55:
             print("Everything is goint to be okay. Enjoy a free ride")
        else:
             bill = 12
             print(f"Adult tickets are ${bill}.130")     
        photo = input("Do you want to take photo? Y/N ? ")
        if photo.lower() == 'y':
            print(f"Total bill with photo {bill+3}")
        else:
             print(f"Total bill without photo {bill}")
else:
    print("You cannot ride the rollercoster")