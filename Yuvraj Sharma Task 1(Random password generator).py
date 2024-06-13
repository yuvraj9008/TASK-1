#CODE BY YUVRAJ SHARMA 
#TECHNOHACKS EDUTECH PYTHON PROGRAMMING INTERNSHIP

#Importing Libraries

import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Please select at least one character type.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


#user input for customization of password
def main():
    length = int(input("Enter the length of the password: "))                                            #user input for length of the password
    use_letters = input("Include letters in the password? (y/n): ").lower() == 'y'              #user input optioning(y/n) letters in the password 
    use_numbers = input("Include numbers in the password? (y/n): ").lower() == 'y'     #user input optioning(y/n) numbers in the password
    use_symbols = input("Include symbols in the password? (y/n): ").lower() == 'y'      #user input optioning(y/n) symbols in the password    
    
    password = generate_password(length, use_letters, use_numbers, use_symbols)   #generation of password as per user's choice
    
    if password:
        print(f"Generated Password: {password}")  #output as random password

if __name__ == "__main__":
    main()