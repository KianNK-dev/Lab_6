# Set top level variables to be utilized within main function
original_password = ''
encoded_password = ''


def password_encode(password):  # defines the following code as the method password_encode
    encoded = ""  # creates an empty string for the encoded password
    for num in password:  # iterates through every character in password with a for loop
        num = int(num)  # casts each character to an integer
        num += 3  # adds three to each integer
        num = str(num)  # casts the added integer to a string
        encoded += num  # concatenates the increased string number to encoded
    return encoded  # returns encoded


# Utility function to handle decoding
def decode(current_password):
    return ''.join(map(lambda x: str((int(x) - 3) % 10), current_password))


def password_decode():
    global original_password, encoded_password
    print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")


def main():
    global original_password, encoded_password  # Access global variables to mutate within main() scope
    loop = True  # creates a variable for whether the program will continue looping and sets it to true
    while loop == True:  # continues to loop the program
        print("Menu")  # prints out the program menu
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        menu_option = int(input("Please enter an option: "))  # asks the user to input a menu option
        if menu_option == 1:  # checks if the user's menu input was 1
            original_password = input(
                "Please enter your password to encode: ")  # prompts the user to input their password
            encoded_password = password_encode(original_password)  # runs the entered password thhrough password_encode
            print("Your password has been encoded and stored!")  # notifies the user that the password has been stored
        if menu_option == 2:  # checks if the user's menu_option was 2
            password_decode()  # Decodes currently global original_password value
        if menu_option == 3:  # checks if the user's menu_options was 3
            loop = False
            break  # breaks the loop


if __name__ == "__main__":
    main()
