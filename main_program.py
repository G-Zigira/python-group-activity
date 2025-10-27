#this program puts everyhitng togehter and oit imports all the functions from the other files as well as validationg the input


from helper_functions import validate_input, convert_to_binary, create_message
from file_manager import save_message, read_message
from greetings import show_intro, show_exit_message


def get_user_info():
    while True:
        name = input("Enter your name: ").strip()
        if not validate_input(name):
            print("Invalid name! Please try again.")
            continue

        age = input("Enter your age: ").strip()
        if not age.isdigit():
            print("Invalid age! Please enter a number.")
            continue

        return name, age


if __name__ == "__main__":
    show_intro()

    name, age = get_user_info()

    # Convert to binary
    name_binary = convert_to_binary(name)
    age_binary = convert_to_binary(age)

    # Create message
    message = create_message(name, age, name_binary, age_binary)

    # Display message and save
    print(message)
    save_message(message)

    # Read message back
    read_message()

    show_exit_message()
