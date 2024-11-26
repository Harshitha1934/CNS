# RC4 Algorithm Implementation in Python

# Initialize plaintext, key, and number of bits to process at a time
plain_text = "001010010010"  # Binary plaintext
key = "101001000001"        # Binary key
n = 3                       # Number of bits to consider at a time

# State vector array (S) and key list
S = [i for i in range(0, 2 ** n)]  # Initialize state vector
key_list = [int(key[i:i + n], 2) for i in range(0, len(key), n)]  # Convert key to integers
pt = [int(plain_text[i:i + n], 2) for i in range(0, len(plain_text), n)]  # Convert plaintext to integers

# Adjust the key list length to match the state vector length
if len(S) != len(key_list):
    key_list += key_list[:len(S) - len(key_list)]


# Key Scheduling Algorithm (KSA)
def KSA(S, key_list):
    """
    Initializes the state vector (S) based on the key.
    Args:
    - S (list): Initial state vector.
    - key_list (list): Key converted into integer list.
    Returns:
    - S (list): Permutated state vector after KSA.
    """
    j = 0
    for i in range(len(S)):
        j = (j + S[i] + key_list[i]) % len(S)
        S[i], S[j] = S[j], S[i]  # Swap values
    return S


# Pseudo-Random Generation Algorithm (PRGA)
def PRGA(S, text_length):
    """
    Generates a keystream of a specified length.
    Args:
    - S (list): State vector after KSA.
    - text_length (int): Length of text to process.
    Returns:
    - key_stream (list): Generated keystream.
    """
    i = j = 0
    key_stream = []
    for _ in range(text_length):
        i = (i + 1) % len(S)
        j = (j + S[i]) % len(S)
        S[i], S[j] = S[j], S[i]  # Swap values
        t = (S[i] + S[j]) % len(S)
        key_stream.append(S[t])
    return key_stream


# XOR function for encryption and decryption
def XOR(input_text, key_stream):
    """
    Performs XOR operation between input text and keystream.
    Args:
    - input_text (list): List of integers representing text.
    - key_stream (list): Generated keystream.
    Returns:
    - list: XOR result.
    """
    return [input_text[i] ^ key_stream[i] for i in range(len(input_text))]


# Encryption function
def encryption():
    """
    Encrypts the plaintext using RC4.
    Returns:
    - cipher_text (list): List of integers representing the ciphertext.
    """
    print("Plain text:", plain_text)
    print("Key:", key)

    # Perform KSA and PRGA
    S_init = KSA(S[:], key_list)  # Initial permutation
    key_stream = PRGA(S_init, len(pt))  # Generate keystream

    # Encrypt plaintext by XORing with keystream
    cipher_text = XOR(pt, key_stream)

    # Convert ciphertext to binary representation
    encrypted_to_bits = ''.join(f"{bin(c)[2:]:0>{n}}" for c in cipher_text)
    print("Cipher text:", encrypted_to_bits)

    return cipher_text


# Decryption function
def decryption(cipher_text):
    """
    Decrypts the ciphertext using RC4.
    Args:
    - cipher_text (list): List of integers representing the ciphertext.
    """
    # Perform KSA and PRGA
    S_init = KSA(S[:], key_list)  # Initial permutation
    key_stream = PRGA(S_init, len(pt))  # Generate keystream

    # Decrypt ciphertext by XORing with keystream
    original_text = XOR(cipher_text, key_stream)

    # Convert decrypted text to binary representation
    decrypted_to_bits = ''.join(f"{bin(p)[2:]:0>{n}}" for p in original_text)
    print("Decrypted text:", decrypted_to_bits)


# Driver Code
cipher_text = encryption()  # Perform encryption
print("---------------------------------------------------------")
decryption(cipher_text)  # Perform decryption
