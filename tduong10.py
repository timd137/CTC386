#Timothy Duong
#Lab 10

def fahrenheit_to_celsius():
    temp_in_F = float(input("Enter the current temperature in Fahrenheit: "))
    temp_in_C = (temp_in_F - 32) * (5/9)
    print("The temperature in Celsius is", temp_in_C)

def word_from_sentence(sentence):
    word = ""
    i = 0
    while i < len(sentence) and sentence[i] != " ": #Words are separated by spaces so this is is how the loop
        word = word + sentence[i]                   #knows when to stop adding characters
        i = i + 1
    return word

def pig_latin_converter(word):
    new_word = ""
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
        new_word = word + "way " #If the word begins with a vowel, then "way" is appended to it
    else:
        for i in range(len(word)):
            if i > 0:
                new_word = new_word + word[i] #If the word begins with a consonant, then the first character is
        new_word = new_word + word[0] + "ay " #moved to the end of the word and "ay" is appended to it
    return new_word

def new_string_from_index(index, string): #Creates a new string that starts at a specified index
    new_string = ""
    while index < len(string):
        new_string = new_string + string[index]
        index = index + 1
    return new_string

name = input("Enter your name: ")

print("Menu")
print("----------")
print("Option 1")
print("Option 2")
print("Option 3")
print("Option 4")
print("Option 5")
print("Option 6")
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

elif option_choice == 6:
    original_sentence = input("Input a sentence to turn into Pig Latin: ")
    new_sentence = original_sentence #For option 6, I used some additional Python features that were not taught
    pig_latin_sentence = ""          #in class: string indexing, string concatenation, and the len() function
    
    i = 0
    while i < len(original_sentence):
          new_word = word_from_sentence(new_sentence)
          pig_latin_sentence = pig_latin_sentence + pig_latin_converter(new_word)
          i = i + len(new_word) + 1 #The + 1 skips the space in a sentence
          new_sentence = new_string_from_index(i, original_sentence) #removes the previous word from new_sentence
          
    print(pig_latin_sentence)
    

