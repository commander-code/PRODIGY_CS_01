# Function to encrypt the text
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

# Function to decrypt the text
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_text += char
    return decrypted_text

# Main program
def main():
    choice = input("Would you like to encrypt or decrypt a message? (e/d): ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid option. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
