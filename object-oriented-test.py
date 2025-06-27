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
    
class ITWorker(Me): # Define Child Class, Inherits everything from Me
    def __init__(self, name, age, specialization):
        super().__init__(name, age) # Call parent constructor
        self.specialization = specialization
        self.certifications = []

    def add_certification(self, cert):
        self.certifications.append(cert)

    def introduce(self):
        base_intro = super().introduce() # Get parent's introduction, returns original introduction
        return f"{base_intro} I'm specializing in {self.specialization}." # then returns ITWorker's Introduction afterwards
    
kyle_student = Me("Kyle", 27) # Object Creation
kyle_student.add_language("Python", 0)
kyle_it = ITWorker("Kyle", 27, "Hybrid Cloud Infrastructure")
kyle_it.add_language("Python", 0)
kyle_it.add_certification("CompTIA A+ (In Progress)")

# print(kyle_student.introduce()) # Print the Introduction
print(kyle_it.introduce()) # Print the Second Introduction
