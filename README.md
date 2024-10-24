# PRODIGY_CS_01
Caesar Cipher Implementation in Python
Overview
This Python code implements the Caesar Cipher algorithm, a simple substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.   
Code Breakdown
caesar_cipher(text, shift) function
This function is responsible for the core encryption/decryption logic.
    1. Initialization: An empty string result is created to store the processed text. 
    2. Iteration: Each character in the input text is iterated over: 
        ◦ Alphabetic Check: If the character is a letter (either uppercase or lowercase), the following steps are performed: 
            ▪ Case Determination: The starting character for the alphabet (either 'A' or 'a') is determined based on the case of the current character. 
            ▪ Shift Calculation: The shifted character's ordinal value is calculated by adding the shift value to the current character's ordinal value, then taking the modulo 26 to ensure the result stays within the alphabet range. 
            ▪ Character Conversion: The calculated ordinal value is converted back to a character using chr(). 
            ▪ Result Update: The shifted character is appended to the result string. 
        ◦ Non-Alphabetic Handling: If the character is not a letter (e.g., punctuation, numbers), it is directly appended to the result string without modification. 
    3. Return: The final encrypted/decrypted text stored in result is returned. 
main() function
This function provides the user interface for interacting with the Caesar Cipher.
    1. Loop: A while loop is used to continuously prompt the user for input until they choose to exit. 
    2. Menu: A menu is displayed to the user, allowing them to choose between encryption, decryption, or quitting. 
    3. Input Handling: Based on the user's choice: 
        ◦ Encryption: Prompts the user for the text to encrypt and the shift value, then calls the caesar_cipher function with the appropriate arguments and prints the encrypted text. 
        ◦ Decryption: Prompts the user for the text to decrypt and the shift value, then calls the caesar_cipher function with a negative shift value (to reverse the encryption) and prints the decrypted text. 
        ◦ Quit: Exits the loop and the program. 
    4. Error Handling: If the user enters an invalid choice, an error message is displayed. 
Usage
    1. Run the Python script. 
    2. Choose the desired operation (encrypt or decrypt) from the menu. 
    3. Enter the text to be processed and the shift value. 
    4. The encrypted or decrypted text will be displayed. 
    5. Repeat steps 2-4 until you choose to quit. 
Note: The Caesar Cipher is a relatively weak encryption algorithm and can be easily broken using frequency analysis. For more secure encryption, consider using stronger algorithms like AES or RSA.
