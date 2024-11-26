import numpy as np

N = 3  # Dimension of the key matrix

def encrypt(key, plaintext):
    """
    Encrypts the plaintext using the Hill cipher encryption algorithm.

    Args:
        key (str): The key string (must form an NxN matrix).
        plaintext (str): The plaintext string of length N.

    Returns:
        str: The encrypted ciphertext.
    """
    # Convert plaintext and key to numerical matrices
    item_matrix = np.array([ord(char) - ord('A') for char in plaintext])  # Convert plaintext to numbers
    key_matrix = np.array([[ord(key[i * N + j]) - ord('A') for j in range(N)] for i in range(N)])  # Key matrix

    # Perform matrix multiplication and modulo operation
    encrypted_matrix = np.dot(key_matrix, item_matrix) % 26
    encrypted_text = ''.join(chr(num + ord('A')) for num in encrypted_matrix)

    return encrypted_text, encrypted_matrix


def decrypt(inverse_key_matrix, encrypted_matrix):
    """
    Decrypts the ciphertext using the inverse key matrix.

    Args:
        inverse_key_matrix (numpy.ndarray): The inverse of the key matrix.
        encrypted_matrix (numpy.ndarray): The encrypted numerical matrix.

    Returns:
        str: The decrypted plaintext.
    """
    # Perform matrix multiplication and modulo operation
    decrypted_matrix = np.dot(inverse_key_matrix, encrypted_matrix) % 26
    decrypted_matrix = np.round(decrypted_matrix).astype(int)  # Round to nearest integer for clean output
    decrypted_matrix = np.where(decrypted_matrix < 0, decrypted_matrix + 26, decrypted_matrix)  # Handle negatives
    decrypted_text = ''.join(chr(num + ord('A')) for num in decrypted_matrix)

    return decrypted_text


if __name__ == "__main__":
    # Key and plaintext
    key = "GYBNQKURP"  # Must form an NxN matrix
    plaintext = "ACT"  # Plaintext must be of length N

    # Encrypt the plaintext
    encrypted_text, encrypted_matrix = encrypt(key, plaintext)
    print(f"Encrypted Message: {encrypted_text}")

    # Predefined inverse key matrix
    inverse_key_matrix = np.array([
        [8, 5, 10],
        [21, 8, 21],
        [21, 12, 8]
    ])  # Inverse of the key matrix (calculated externally)

    # Decrypt the ciphertext
    decrypted_text = decrypt(inverse_key_matrix, encrypted_matrix)
    print(f"Decrypted Message: {decrypted_text}")
