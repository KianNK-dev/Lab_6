def password_encode(password): #defines the following code as the method password_encode
    encoded = "" #creates an empty string for the encoded password
    for num in password: #iterates through every character in password with a for loop
        num = int(num) #casts each character to an integer
        num += 3 #adds three to each integer
        num = str(num) #casts the added integer to a string
        encoded += num #concatenates the increased string number to encoded
    return encoded #returns encoded

if __name__ == "__main__": #checks that the file runs correctly before running the main method
    loop = True #creates a variable for whether the program will continue looping and sets it to true
    while loop == True: #continues to loop the program
        print("Menu/n-------------/n1. Encode/n2. Decode/n3. Quit") #prints out the program menu
        print() #line break
        menu_option = int(input("Please enter an option: ")) #asks the user to input a menu option
        if menu_option == 1: #checks if the user's menu input was 1
            og_password = input("Please enter your password to encode: ") #prompts the user to input their password
            password = password_encode(og_password) #runs the entered password thhrough password_encode
            print("Your password has been encoded and stored!") #notifies the user that the password has been stored
        if menu_option == 2: #checks if the user's menu_option was 2
            pass
        if menu_option == 3: #checks if the user's menu_options was 3
            loop = False #sets loop to false
            break #breaks the loop
        print() #line break between loops
