""" Text to Morse Code Converter

 This program converts text message into Morse code message

"""

# User's input message converted into uppercase and stored in variable
user_message = input('What is your message? ').upper()
# print(user_message)

# Create an Empty Morse Code Message List
morse_code_list = []

# Creating a morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',

    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '!': '-.-.--', '@': '.--.-.', ' ': '/'
}

# Iterate over the user_message and accessing the morse_code_dict items to obtain values using a for loop
for letter in user_message:
    # Adding the value into the empty morse_code_list
    morse_code_list.append(morse_code_dict[letter])

# Iterating the morse_code_list converting into a string with spaces and storing it into a variable
morse_code_msg = " ".join(str(item) for item in morse_code_list)

# Print the output
print(f'Your Morse Code message is "{morse_code_msg}"')


