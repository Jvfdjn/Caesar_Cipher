# Importing the 'art_str' variable from the 'art' module
from art import art_str

# Printing the ASCII art stored in the 'art_str' variable
print(art_str)

# Initializing the variable 'should_continue' with the value 'True'
should_continue = True

# Defining the 'caesar' function that takes a start text, shift amount, and cipher direction as input
def caesar(start_text, shift_amount, cipher_direction):
    # Initializing an empty string to store the encrypted/decrypted text
    end_text = ""
    
    # Checking if the cipher direction is 'decode' and adjusting the shift amount accordingly
    if cipher_direction == "decode":
        shift_amount *= -1
    
    # Iterating through each letter in the start text
    for letter in start_text:
        # Checking if the letter is in the alphabet list
        if letter in alphabet:
            # Finding the position of the letter in the alphabet
            position = alphabet.index(letter)
            
            # Calculating the new position after applying the shift
            new_position = position + shift_amount
            
            # Appending the shifted letter to the end text
            end_text += alphabet[new_position]
        else:
            # If the letter is not in the alphabet, appending it to the end text as is
            end_text += letter
    
    # Printing the result of the encryption/decryption
    print(f"Here's the {cipher_direction}d result: {end_text}")

# Starting a while loop that continues as long as 'should_continue' is True
while should_continue:
    # Defining the alphabet list
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
                's','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
    
    # Taking input from the user for the cipher direction (encode/decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt\n")
    
    # Taking input from the user for the text to be encrypted/decrypted
    text = input("Type your message:\n").lower()
    
    # Taking input from the user for the shift amount
    shift = int(input("Type the shift number: \n"))
    
    # Ensuring that the shift is within the range of the alphabet
    shift = shift % 26
    
    # Calling the 'caesar' function with the provided inputs
    caesar(text, shift, direction)

    # Taking input from the user to determine whether to continue the loop
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    # Checking if the user wants to continue or not
    if result == "no":
        # Setting 'should_continue' to False to exit the loop
        should_continue = False
        # Printing a goodbye message
        print("Goodbye!")
