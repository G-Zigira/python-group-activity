#this is the first document is for binary conversion, input validation and it makes the message after the user is done with input 

# function to check if the user input is vaild
def validate_input(user_input):
    return bool(user_input and isinstance(user_input, str))

# funciton to convert the insert text to binary
def convert_to_binary(text):
    if text.isdigit():
        return bin(int(text))
    else:
        return ' '.join(format(ord(char), '08b') for char in text)

# function will merge all the variable in one message using f string
def create_message(name, age, name_binary, age_binary):
    message = (
        f"Hello {name}, you are {age} years old!\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}"
    )
    return message