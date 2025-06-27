# This is a test

## Basic Printing
name = "Kyle"
age = 27
favorite_languages = ["Python", "C++", "Java"] # list
years_experience = {"C++": 1, "Java": 1, "Python": 0} # dictionary
isLearning = True # boolean

print(f"My name is {name} and I am {age} years old!") # print statement with f formatting
### Printing with If Statement
if isLearning: # if statement
    print(f"I am currently learning {favorite_languages[0]} and I currently have {years_experience['Python']} years of experience.") # printing with list and dictionary types

### Printing with For Loop
for language in favorite_languages: # loop index through favoriteLanguages, displaying the language known and years of experience
    print(f"{language}: {years_experience[language]} years of experience")

### Printing with Error Catching
language_to_check = "Rust"
try:
    # You idiot
    print(years_experience[language_to_check])
except KeyError:
    # What do?
    print(f"You might want to learn {language_to_check} first!")

def function_test():
    print(f"Enter 1 number followed by enter, 4 times, please!")
    i = int(input("Input a number!"))
    j = int(input("Input another number!"))
    k = int(input("Input yet, another number!"))
    l = int(input("You thought we were done? Input one more number!"))
    # Do things and stuff
    s = i+j+k+l
    print(f"The sum is {s}, why not just use a calculator?")

function_test()