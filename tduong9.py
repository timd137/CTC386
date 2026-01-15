#Timothy Duong
#Lab 9
#GitHub test comment

def fahrenheit_to_celsius():
    temp_in_F = float(input("Enter the current temperature in Fahrenheit: "))
    temp_in_C = (temp_in_F - 32) * (5/9)
    print("The temperature in Celsius is", temp_in_C)

name = input("Enter your name: ")

print("Menu")
print("----------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("----------")

print("Hello", name, ", enter a number to choose an option: ")
option_choice = int(input())

if option_choice == 1:
    print("Why can't sailors learn the alphabet?")
    print("Because they always get lost at C!")
elif option_choice == 2:
    for i in range(15):
        print(name)
elif option_choice == 3:
    num = int(input("Enter a number: "))
    for i in range(num):
        print("All the world's a stage, and all the men and women merely players.")
elif option_choice == 4:
    number = 5
    guess = 0
    while guess != number:
        guess = int(input("Guess a number between 0-100 inclusive: "))
        if guess < 0 or guess > 100:
            print("Your guess is out of range - it should be between 0-100 inclusive.")
        elif guess != number:
            if guess > number:
                print("Your guess is too high. Please guess again.")
            elif guess < number:
                print("Your guess is too low. Please guess again.")
        elif guess == number:
            print("You won! Your guess of", guess, "is equal to the intended number,", number)
elif option_choice == 5:
    fahrenheit_to_celsius()

