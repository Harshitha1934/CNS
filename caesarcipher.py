def encrypt(text, key):
    """
    Encrypts the input text using the Caesar cipher with the given key.
    
    Args:
        text (str): The plaintext to encrypt.
        key (int): The cipher key (shift value).
    
    Returns:
        str: The encrypted message.
    """
    encrypted_text = ""
    for char in text:
        if char.islower():  # Encrypt lowercase letters
            encrypted_text += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():  # Encrypt uppercase letters
            encrypted_text += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.isdigit():  # Encrypt digits
            encrypted_text += chr((ord(char) - ord('0') + key) % 10 + ord('0'))
        else:  # Invalid character
            raise ValueError("Invalid character in message. Only alphanumeric characters are allowed.")
    return encrypted_text


def decrypt(text, key):
    """
    Decrypts the input text encrypted with the Caesar cipher using the given key.
    
    Args:
        text (str): The encrypted message to decrypt.
        key (int): The cipher key (shift value).
    
    Returns:
        str: The decrypted message.
    """
    decrypted_text = ""
    for char in text:
        if char.islower():  # Decrypt lowercase letters
            decrypted_text += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        elif char.isupper():  # Decrypt uppercase letters
            decrypted_text += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.isdigit():  # Decrypt digits
            decrypted_text += chr((ord(char) - ord('0') - key) % 10 + ord('0'))
        else:  # Invalid character
            raise ValueError("Invalid character in message. Only alphanumeric characters are allowed.")
    return decrypted_text


def main():
    message = input("Enter a message to encrypt: ")
    key = int(input("Enter the key: "))

    try:
        encrypted_message = encrypt(message, key)
        print(f"Encrypted message: {encrypted_message}")

        decrypted_message = decrypt(encrypted_message, key)
        print(f"Decrypted message: {decrypted_message}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
