def encrypt(message, key):
    """
    Encrypts the message using the given substitution cipher key.

    Args:
        message (str): The plaintext message to be encrypted.
        key (str): The substitution key, a string of 26 lowercase letters.

    Returns:
        str: The encrypted message.
    """
    encrypted_message = ""
    for char in message:
        if 'a' <= char <= 'z':  # Encrypt lowercase letters
            encrypted_message += key[ord(char) - ord('a')]
        else:
            encrypted_message += char  # Leave other characters unchanged
    return encrypted_message


def decrypt(message, key):
    """
    Decrypts the message using the given substitution cipher key.

    Args:
        message (str): The encrypted message to be decrypted.
        key (str): The substitution key, a string of 26 lowercase letters.

    Returns:
        str: The decrypted message.
    """
    # Create a reverse mapping for decryption
    reverse_key = {key[i]: chr(i + ord('a')) for i in range(26)}

    decrypted_message = ""
    for char in message:
        if char in reverse_key:  # Decrypt only characters present in the key
            decrypted_message += reverse_key[char]
        else:
            decrypted_message += char  # Leave other characters unchanged
    return decrypted_message


def main():
    key = input("Enter the substitution key (26 lowercase letters in random order): ").strip()
    if len(key) != 26 or not all('a' <= char <= 'z' for char in key):
        print("Invalid key. Please provide exactly 26 lowercase letters.")
        return

    message = input("Enter the message to encrypt: ").strip()
    
    encrypted_message = encrypt(message, key)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()
