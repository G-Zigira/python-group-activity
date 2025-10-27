#this python file saves the message and accepts the said message as input

def save_message(message):
    try:
        with open("user_message.txt", "w", encoding="utf-8") as file:
            file.write(message)
        print("The message has been saved successfully.")
    except Exception as e:
        print(f"Error saving message: {e}")


def read_message():
    try:
        print("Reading the saved message...")
        with open("user_message.txt", "r", encoding="utf-8") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"Error in reading file: {e}")
