# Character Creator Program
# Output Example: 27 year old, Black Human Male, named Jerimah Mathers

# Random race and species (allow user to opt out of random output.).
# Randomize age within range. (i.e. is character a minor, adult, or elderly)

# GLOBAL VARIABELS
GENDER = ['Male', 'Female']

HUMAN_RACES = ['Black-American', 'White-American', 'Asian-American', 'Hispanic-American', 'Native American', 'Pacific Islander', 'Middle Eastern', 
               'Japanese', 'Chinese', 'Korean', 'Indian', 'Filipino', 'Vietnamese', 'German', 'French', 'Italian', 'British', 'Irish', 'Russian', 'Polish', 'Scandinavian',
               'African', 'Caribbean', 'Latin American', 'Egyptian', 'Arab', 'Persian', 'Turkish', 'Jewish', 'Greek']
# Age ranges for humans for random age generation. The user can select a specific age or have it be randomly generated within these ranges.
# Dictionary with the age ranges for humans. The keys are the age categories (minor, adult, elderly) and the values are tuples containing the minimum and maximum ages for each category. 
# The user can select a specific age or have it be randomly generated within these ranges.
HUMAN_AGE_RANGE = {
    'Minor': (0, 17), 
    'Adult': (18, 64),
    'Elderly': (65, 120)
}
# Height ranges for humans for random height generation. The user can select a specific height or have it be randomly generated within these ranges.
# Height is measured in inches. The user can select a specific height or have it be randomly generated within these ranges.
# Dictionary with the height ranges for humans. The keys are the height categories (short, average, tall) 
# Values are tuples containing the minimum and maximum heights in inches for each category.
HUMAN_HEIGHT_RANGE = {
    'Short': (40, 59), # 5 feet or shorter  
    'Average': (60, 72), # between 5 feet and 6 feet
    'Tall': (73, 96) # 6 feet or taller
}

# Elf Global Variables
ELF_RACES = ['High Elf', 'Wood Elf', 'Dark Elf']
ELF_AGE_RANGE = {
    'Minor': (0, 100),
    'Adult': (101, 500),
    'Elderly': (501, 1000)
}
ELF_HEIGHT_RANGE = {
    'Short': (36, 59),
    'Average': (60, 72),
    'Tall': (73, 128)
}

# Dwarf Global Variables
DWARF_RACES = ['Mountain Dwarf', 'Hill Dwarf', 'Duergar']
DWARF_AGE_RANGE = {
    'Minor': (0, 100),
    'Adult': (101, 500),
    'Elderly': (501, 1000)
}
DWARF_HEIGHT_RANGE = {
    'Short': (32, 39),
    'Average': (40, 47),
    'Tall': (48, 56)
}

# Demon Global Variables
DEMON_RACES = ['Balor', 'Incubus', 'Succubus']
DEMON_AGE_RANGE = {
    'Minor': (0, 100),
    'Adult': (101, 500),
    'Elderly': (501, 1000)
}
DEMON_HEIGHT_RANGE = {
    'Short': (36, 59),
    'Average': (60, 72),
    'Tall': (73, 128)
}

# Dependency imports
import random

# Function to select the species of the character. This will be the first step in the character creation process.
def species_select():
    print('\n===============================================================')
    print('\n\t---- Species Selection ----')
    print('\n===============================================================')
    print('\nThe available species are:')
    print('Human\nElf\nDwarf\nDemon')
    species = input('\nPlease select the species for this Character: ')
    if species == 'human' or species == 'Human':

        # Calling the human() function to select the traits of the character based on the species selected. The traits will then be printed in a readable format by calling the print_character_traits() function.
        race, gender, age, name, height = human() 
        # Passing the species and the traits of the character as arguments to the print_character_traits() function to print the traits in a readable format.
        print_character_traits(species, race, gender, age, name, height)

    elif species == 'elf' or species == 'Elf':
        race, gender, age, name, height = elf()
        print_character_traits(species, race, gender, age, name, height)
    elif species == 'dwarf' or species == 'Dwarf':
        pass
        # dwarf()
    elif species == 'demon' or species == 'Demon':
        pass
        # demon()
    else:
        print('Invalid input. Please enter a valid species.')
        species_select()
    return species


# Functions to select the traits of the character based on the species selected. These functions will be called in the species_select() function.
def human():
    # Race selection (allow user to opt out of random output.)
    print('\n---------------------------------------------------------------')
    print('List of human races:')
    # Outputting the list of available races.
    for race in HUMAN_RACES:
        print(f'- {race:<20}')
        
    race_selection_choice = input('\nWould you like to select the race or have it be random? (y/n): ')
    if race_selection_choice == 'y':
        race = random.choice(HUMAN_RACES)
    elif race_selection_choice == 'n':
        race = input('\nWhat race is this character? ') 
    else:
        print('Invalid input. Please enter y or n.')

    # Gender selection (allow user to opt out of random output.)
    gender_selection_choice = input('\nWould you like to select the gender or have it be random? (y/n): ')
    if gender_selection_choice == 'y':
        gender = random.choice(GENDER)
        print(f'\nThe gender of this character is {gender}.')
    elif gender_selection_choice == 'n':
        gender = input('\nWhat gender is this character? ')
    else:
        print('Invalid input. Please enter y or n.')

    # Age selection (allow user to opt out of random output.)
    age_selection_choice = input('\nWould you like to select the age or have it be random? (y/n): ')
    if age_selection_choice == 'y':

        # Prompt the user to select an age range for the character. The age will then be randomly generated within that range.
        age_range_choice = input('\nWould you like the age to be a minor, adult, or elderly? (minor/adult/elderly): ')
        if age_range_choice == 'minor' or age_range_choice == 'Minor':
            age = random.randint(HUMAN_AGE_RANGE['Minor'][0], HUMAN_AGE_RANGE['Minor'][1])
        elif age_range_choice == 'adult' or age_range_choice == 'Adult':
            age = random.randint(HUMAN_AGE_RANGE['Adult'][0], HUMAN_AGE_RANGE['Adult'][1])
        elif age_range_choice == 'elderly' or age_range_choice == 'Elderly':
            age = random.randint(HUMAN_AGE_RANGE['Elderly'][0], HUMAN_AGE_RANGE['Elderly'][1])

    # If the user opts out of random age generation, they will be prompted to enter a specific age for the character.
    elif age_selection_choice == 'n':
        age = input('\nWhat age is this character? ')
    else:
        print('Invalid input. Please enter y or n.')

    # Name selection (allow user to opt out of random output.)
    name_selection_choice = input('\nWould you like to select the name or have it be random? (y/n): ')
    if name_selection_choice == 'y':
        # If the user opts for random name generation, they will be prompted to enter the file containing the first names list and the file containing the surnames list. 
        # The program will then randomly select a first name and a surname from the respective lists to create the character's full name.

        if gender == 'Male':
            first_name_file =  open('male_human_names.txt', 'r') # opening file containing first names to read and output a random first name
            first_name_list = first_name_file.read().splitlines()
            first_name = random.choice(first_name_list)

            # opening surnames file to read and output a random surname
            surname_file = open('human_surnames.txt', 'r') # opening file containing surnames to read and output a random surname
            surname_list = surname_file.read().splitlines()
            surname = random.choice(surname_list)
            name = f'{first_name} {surname}'

        elif gender == 'Female':
            first_name_file =  open('female_human_names.txt', 'r') # opening file containing first names to read and output a random first name
            first_name_list = first_name_file.read().splitlines()
            first_name = random.choice(first_name_list)

            # opening surnames file to read and output a random surname
            surname_file = open('human_surnames.txt', 'r') # opening file containing surnames to read and output a random surname
            surname_list = surname_file.read().splitlines()
            surname = random.choice(surname_list)
            name = f'{first_name} {surname}'

    elif name_selection_choice == 'n':
        name = input('\nWhat is the name of this character? ')
    else:
        print('Invalid input. Please enter y or n.')

    # Height selection (allow user to opt out of random output.)
    height_selection_choice = input('\nWould you like to select the height or have it be random? (y/n): ')
    if height_selection_choice == 'y':

        # Prompt the user to select a height range for the character. The height will then be randomly generated within that range.
        height_range_choice = input('\nWould you like the height to be short, average, or tall? (short/average/tall): ')
        if height_range_choice == 'short' or height_range_choice == 'Short':
            height = random.randint(HUMAN_HEIGHT_RANGE['Short'][0], HUMAN_HEIGHT_RANGE['Short'][1])
        elif height_range_choice == 'average' or height_range_choice == 'Average':
            height = random.randint(HUMAN_HEIGHT_RANGE['Average'][0], HUMAN_HEIGHT_RANGE['Average'][1])
        elif height_range_choice == 'tall' or height_range_choice == 'Tall':
            height = random.randint(HUMAN_HEIGHT_RANGE['Tall'][0], HUMAN_HEIGHT_RANGE['Tall'][1])
    
    # If the user opts out of random height generation, they will be prompted to enter a specific height for the character.
    elif height_selection_choice == 'n':
        height = input(print('\nWhat is the height of this character in inches? '))
    else:
        print('Invalid input. Please enter y or n.')
    
    # converting the height from inches to feet and inches for easier readability.
    height = height_conversion(height) # passing the height in inches as an argument to the height_conversion function to convert it to feet and inches for easier readability.

    # returning the traits of the character as a tuple to be used in the print_character_traits() function to print the traits in a readable format.
    return race, gender, age, name, height


def elf():
    print('\n----------------------------------------------------------------')

    # Elf race seleciton
    print('List of available races:')
    for race in ELF_RACES:
        print(f'- {race:<20}')
    race_selection_choice = input('\nWould you like to select the race or have it be random? (y/n): ')
    if race_selection_choice == 'y':
        race = random.choice(ELF_RACES)
    elif race_selection_choice == 'n':
        input('\nWhat race is this character? ')
    else:
        print('Invalid input. Please enter y or n.')

    # Elf gender selection
    gender_selection_choice = input('\nWould you like to select the gender or have it be random? (y/n): ')
    if gender_selection_choice == 'y':  
        gender = random.choice(GENDER)
        print(f'\nThe gender of this character is {gender}.')
    elif gender_selection_choice == 'n':
        input('\nWhat gender is this character? ')
    else:
        print('Invalid input. Please enter y or n.')

    # Elf age selection
    age_selection_choice = input('\nWould you like to select the age or have it be random? (y/n): ')
    if age_selection_choice == 'y':

        # Prompt the user to select an age range for the character. The age will then be randomly generated within that range.
        age_range_choice = input('\nWould you like the age to be a minor, adult, or elderly? (minor/adult/elderly): ')
        if age_range_choice == 'minor' or age_range_choice == 'Minor':
            age = random.randint(ELF_AGE_RANGE['Minor'][0], ELF_AGE_RANGE['Minor'][1])
        elif age_range_choice == 'adult' or age_range_choice == 'Adult':
            age = random.randint(ELF_AGE_RANGE['Adult'][0], ELF_AGE_RANGE['Adult'][1])
        elif age_range_choice == 'elderly' or age_range_choice == 'Elderly':
            age = random.randint(ELF_AGE_RANGE['Elderly'][0], ELF_AGE_RANGE['Elderly'][1])

    # Elf name selection
    name_selection_choice = input('\nWould you like to select the name or have it be random? (y/n): ')
    if name_selection_choice == 'y':
        if gender == 'Male':
            first_name_file =  open('male_elf_names.txt', 'r') # opening file containing first names to read and output a random first name
            first_name_list = first_name_file.read().splitlines()
            first_name = random.choice(first_name_list)

            # opening surnames file to read and output a random surname
            surname_file = open('elf_surnames.txt', 'r') # opening file containing surnames to read and output a random surname
            surname_list = surname_file.read().splitlines()
            surname = random.choice(surname_list)
            name = f'{first_name} {surname}'

        if gender =='Female':
            # opening file containing first names to read and output a random first name
            first_name_file = open('female_elf_names.txt', 'r') 
            first_name_list = first_name_file.read().splitlines()
            first_name = random.choice(first_name_list)

            # opening surnames file to read and output a random surname
            surname_file = open('elf_surnames.txt', 'r')
            surname_list = surname_file.read().splitlines()
            surname = random.choice(surname_list)
            name = f'{first_name} {surname}'

    elif name_selection_choice == 'n':
        name = input('\nWhat is the name of this character? ')
    else:
        print('Invalid input. Please enter y or n.')

    # Elf height selection
    height_selection_choice = input('\nWould you like to select the height or have it be random? (y/n): ')
    if height_selection_choice == 'y':

        # Prompt the user to select a height range for the character. The height will then be randomly generated within that range.
        height_range_choice = input('\nWould you like the height to be short, average, or tall? (short/average/tall): ')
        if height_range_choice == 'short' or height_range_choice == 'Short':
            height = random.randint(ELF_HEIGHT_RANGE['Short'][0], ELF_HEIGHT_RANGE['Short'][1])
        elif height_range_choice == 'average' or height_range_choice == 'Average':
            height = random.randint(ELF_HEIGHT_RANGE['Average'][0], ELF_HEIGHT_RANGE['Average'][1])
        elif height_range_choice == 'tall' or height_range_choice == 'Tall':
            height = random.randint(ELF_HEIGHT_RANGE['Tall'][0], ELF_HEIGHT_RANGE['Tall'][1])

    elif height_selection_choice == 'n':
        height = input(print('\nWhat is the height of this character in inches? '))
    else:
        print('Invalid input. Please enter y or n.')

    height = height_conversion(height) 

    return race, gender, age, name, height


def dwarf():
    print('\n----------------------------------------------------------------')

    # Dwarf race seleciton
    print('List of available races:')
    for race in DWARF_RACES:
        print(f'- {race:<20}')
    race_selection_choice = input('\nWould you like to select the race or have it be random? (y/n): ')
    if race_selection_choice == 'y':
        race = random.choice(DWARF_RACES)
    elif race_selection_choice == 'n':
        input('\nWhat race is this character? ')
    else:
        print('Invalid input. Please enter y or n.')
    
    # Dwarf gender selection
    
    


def demon():
    pass


# Function to convert height from inches to feet and inches for easier readability.
def height_conversion(height_in_inches): # passing the height in inches as an argument to the height_conversion function to convert it to feet and inches for easier readability.
    feet = height_in_inches // 12
    inches = height_in_inches % 12
    return f'{feet} feet {inches} inches'


# Output function to print the character's traits in a readable format.
def print_character_traits(species, race, gender, age, name, height):
    print('\n===============================================================')
    print('\t---- Character Traits ----')
    print('===============================================================')
    print(f'\nSpecies: {species}') # passing species as an argument in {} to print the species of the character in a readable format.
    print(f'Race: {race}')
    print(f'Gender: {gender}')
    print(f'Age: {age}')
    print(f'Height: {height}')
    print(f'Name: {name}')

    # output to character to text file
    character_traits = f'Species: {species}\nRace: {race}\nGender: {gender}\nAge: {age}\nHeight: {height}\nName: {name}\n'
    file_name = input('\nPlease enter the file name to save this character\'s traits (i.e. [name]_character_traits.txt): ')
    with open(file_name, 'w') as file:
        file.write(character_traits)

    # After printing the character's traits, the program will ask the user if they want to create another character or exit the program by calling the keep_going() function.
    keep_going()


# Function to ask the user if they want to create another character or exit the program.
def keep_going():
    while True:
        keep_going = input('\nWould you like to make another character? (y/n): ')
        if keep_going == 'y':
            print('\nGreat! Let\'s start with the species of your character.')
            species_select()
        elif keep_going == 'n':
            print('\nThank you for using the Character Creator Program! Goodbye!')
            break
        else:
            print('Invalid input. Please enter y or n.')


def main():
    print('--------------------------------------------------------------')
    print('\t---- Welcome to the Character Creator Program! ----')
    print('\nThis program will create a random character for you to use in your story.')
    print('\nYou can choose to have the character be completely random, or you can choose certain traits for the character.')
    print('\nLet\'s get started!')
    print('--------------------------------------------------------------')
    # Starting the character creation process by calling the species_select() function to select the species of the character.
    species_select()

if __name__ == '__main__':
    main()