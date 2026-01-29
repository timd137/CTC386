#Timothy Duong
#CTC 386 Final Exam Question 1


print("Menu")
print("----------")
print("Option 1")
print("Option 2")
print("Option 3")
print("----------")

option_choice = int(input("Enter a number to choose an option: "))

if option_choice == 1:
    name = input("Enter your name: ")
    print("Hey", name, "- what do you call a bear with no teeth?")
    print("A gummy bear!")

if option_choice == 2:
    for i in range(20):
        print("Tacos")

if option_choice == 3:
    number = 1
    while number != 0:
        number = int(input("Enter a number: "))
        if number != 0:
            print("Warning: incorrect number")
