# Rail Fence Cipher - Encryption
def rail_fence_encrypt(text, key):
    """
    Encrypts the given text using the Rail Fence Cipher technique.

    Args:
    - text (str): The plaintext to encrypt.
    - key (int): The number of rails (rows).

    Returns:
    - str: The encrypted text.
    """
    # Create a list to hold strings for each rail
    rails = ['' for _ in range(key)]
    direction_down = False  # Tracks direction (up or down in the rails)
    row = 0  # Starting at the first rail

    # Traverse the text and place each character in the appropriate rail
    for char in text:
        rails[row] += char  # Append character to the current rail
        # Change direction if we're at the top or bottom rail
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        # Move to the next rail (up or down)
        row += 1 if direction_down else -1

    # Join all rails to produce the encrypted text
    return ''.join(rails)

# Rail Fence Cipher - Decryption
def rail_fence_decrypt(encrypted_text, key):
    """
    Decrypts the given text encrypted using the Rail Fence Cipher technique.

    Args:
    - encrypted_text (str): The text to decrypt.
    - key (int): The number of rails (rows).

    Returns:
    - str: The decrypted text.
    """
    n = len(encrypted_text)  # Length of the encrypted text
    # Create a matrix to mark the zigzag pattern
    zigzag = [['\n' for _ in range(n)] for _ in range(key)]
    direction_down = None
    row, col = 0, 0

    # Step 1: Mark positions in the zigzag pattern
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Mark this position with a placeholder
        zigzag[row][col] = '*'
        col += 1
        # Move up or down the rails
        row += 1 if direction_down else -1

    # Step 2: Fill the zigzag pattern with the encrypted text
    index = 0
    for i in range(key):
        for j in range(n):
            if zigzag[i][j] == '*' and index < n:
                zigzag[i][j] = encrypted_text[index]  # Place the character
                index += 1

    # Step 3: Read the zigzag pattern to reconstruct the original text
    result = []
    row, col = 0, 0
    for i in range(n):
        if row == 0:
            direction_down = True
        elif row == key - 1:
            direction_down = False

        # Collect characters from the zigzag
        if zigzag[row][col] != '\n':
            result.append(zigzag[row][col])
        col += 1
        # Move up or down the rails
        row += 1 if direction_down else -1

    return ''.join(result)

# Example Usage
if __name__ == "__main__":
    text = "HELLORAILFENCE"
    key = 3

    # Encrypt the text
    encrypted = rail_fence_encrypt(text, key)
    print("Encrypted:", encrypted)

    # Decrypt the text
    decrypted = rail_fence_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
