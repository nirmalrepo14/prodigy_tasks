def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base if mode == 'encrypt' else (ord(char) - base - shift) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'D':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher(message, shift, mode='decrypt')
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
'''#output
Enter 'E' for encryption or 'D' for decryption: E
Enter the message to encrypt: hellothisiscyphertest
Enter the shift value: 6
Encrypted message: nkrruznoyoyievnkxzkyz '''
