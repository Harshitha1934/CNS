def vigenere_encrypt(text, key):
    """
    Encrypt a given text using the Vigenère cipher with the provided key.

    Args:
    - text (str): The plaintext to encrypt (assumes uppercase letters only).
    - key (str): The key used for encryption (assumes uppercase letters only).

    Returns:
    - str: The encrypted text.
    """
    # Extend the key to match the length of the text
    extended_key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]

    # Encrypt each character
    encrypted_text = ''.join(
        chr(((ord(text[i]) - 65 + ord(extended_key[i]) - 65) % 26) + 65)
        for i in range(len(text))
    )
    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    """
    Decrypt a given text using the Vigenère cipher with the provided key.

    Args:
    - encrypted_text (str): The encrypted text to decrypt (assumes uppercase letters only).
    - key (str): The key used for decryption (assumes uppercase letters only).

    Returns:
    - str: The decrypted text.
    """
    # Extend the key to match the length of the encrypted text
    extended_key = (key * (len(encrypted_text) // len(key))) + key[:len(encrypted_text) % len(key)]

    # Decrypt each character
    decrypted_text = ''.join(
        chr(((ord(encrypted_text[i]) - 65 - (ord(extended_key[i]) - 65) + 26) % 26) + 65)
        for i in range(len(encrypted_text))
    )
    return decrypted_text

# Example usage
if __name__ == "__main__":
    text = "HELLO"  # Plaintext (uppercase letters only)
    key = "KEY"     # Key (uppercase letters only)

    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)

    print("Original Text:", text)
    print("Encryption Key:", key)
    print("Encrypted Text:", encrypted)
    print("Decrypted Text:", decrypted)
