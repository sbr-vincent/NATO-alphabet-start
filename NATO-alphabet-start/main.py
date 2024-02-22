import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

new_dict = {name : value for [name, value] in zip(student_dict["student"], student_dict["score"])}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass


student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# letters = data['letter'].to_list()
# codes = data['code'].to_list()
#
# nato_dict = {letter: code for [letter, code] in zip(letters, codes)}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a name: ")
user_list = [nato_dict[letter.upper()] for letter in user_input]
print(user_list)

