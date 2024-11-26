import random

# Function to generate a random key of the same length as the plaintext
def generate_key(plaintext_length):
    """
    Generate a random key of the given length.

    Args:
    - plaintext_length (int): The length of the plaintext.

    Returns:
    - str: A random key consisting of uppercase letters.
    """
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(plaintext_length))
    return key

# Function to encrypt plaintext using XOR encryption
def encrypt(plaintext, key):
    """
    Encrypt the plaintext using XOR with the given key.

    Args:
    - plaintext (str): The plaintext to encrypt.
    - key (str): The encryption key.

    Returns:
    - str: The encrypted ciphertext.
    """
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext

# Function to decrypt ciphertext using XOR decryption
def decrypt(ciphertext, key):
    """
    Decrypt the ciphertext using XOR with the given key.

    Args:
    - ciphertext (str): The ciphertext to decrypt.
    - key (str): The decryption key.

    Returns:
    - str: The decrypted plaintext.
    """
    decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
    return decrypted_text

# Main execution
if __name__ == "__main__":
    plaintext = "HELLOO"  # The input plaintext
    key = generate_key(len(plaintext))  # Generate a random key of the same length as the plaintext

    print("Plaintext:", plaintext)
    print("Key:", key)

    # Encrypt the plaintext
    ciphertext = encrypt(plaintext, key)
    print("Ciphertext (in altered form):", end=' ')
    for i in range(len(ciphertext)):
        # Represent ciphertext characters in uppercase alphabet letters
        print(chr((ord(ciphertext[i]) % 26) + ord('A')), end='')
    print()  # Newline for formatting

    # Decrypt the ciphertext back to plaintext
    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)
