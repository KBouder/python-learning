# Object Oriented Test Script

class Me: # Define Class
    def __init__(self, name, age): # Initialization
        self.name = name
        self.age = age
        self.languages = []
        self.years_experience = {}

    def add_language(self, language, years): # Function Declaration
        if language not in self.languages: # If Language isn't in the list, append it
            self.languages.append(language)
        self.years_experience[language] = years

    def get_total_languages(self): # Getter Function
        return len(self.languages)
    
    def introduce(self): # Get Introduction Function
        language_list = ', '.join(self.languages) # Take language list, and combine them with ', ' separator
        return f"Hi, my name is {self.name}, I am {self.age} years old. I know {language_list} programming languages. I know {len(self.languages)} languages in total!"
    
kyle = Me("Kyle", 27) # Object Creation
kyle.add_language("C++", 1)
kyle.add_language("Java", 1)
kyle.add_language("Python", 0)

print(kyle.introduce()) # Print The Introduction

