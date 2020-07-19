# Dictionary practice
# it takes in the phone number and prints those in letter

number_dictionary = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

# 1st solution
phone_number = input("Phone: ")
letter = ''
for number in phone_number:
    if number in number_dictionary:
        letter += number_dictionary[number] + " "
print(letter)

# 2nd solution
"""
phone_number = input("Phone: ")
letter = ''
for number in phone_number:
    letter += number_dictionary.get(number, "!") + " "

print(letter)

"""