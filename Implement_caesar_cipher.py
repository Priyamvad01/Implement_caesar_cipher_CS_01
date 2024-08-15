def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    print("Ensure you have permission to use this tool responsibly and only for educational purposes.")
    
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice!")
        return

    text = input("Enter the message: ").strip()
    
    while True:
        shift_input = input("Enter the shift value: ").strip()
        try:
            shift = int(shift_input)
            break
        except ValueError:
            print("Invalid shift value! Please enter a valid integer.")

    if choice == 'E':
        result = encrypt(text, shift)
        print("Encrypted message:", result)
    elif choice == 'D':
        result = decrypt(text, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()