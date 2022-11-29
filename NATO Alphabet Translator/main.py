student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

# Get pandas to read the CSV and save as nato.
nato = pandas.read_csv("nato_phonetic_alphabet.csv")
# Run through nato and create a dictionary using the letter column as they key and the code column as the value.
nato_dict = {nato.letter[index]: nato.code[index] for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
is_word = False

while not is_word:
    # Get the user to enter a word, capitalize it.
    answer = input("Type word: ").upper()
    # Search nato_dict for each letter in the word and add it's code to word_list. Then print it.
    try:
        word_list = [nato_dict[letter] for letter in answer]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word_list)
        is_word = True
