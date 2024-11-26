from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_blowfish(user_input):
    """
    Encrypts a user-provided string using Blowfish encryption.
    
    Args:
    - user_input (str): The plaintext string to be encrypted.
    
    Returns:
    - key (bytes): The encryption key.
    - iv (bytes): The initialization vector used for encryption.
    - encrypted_data (str): The encrypted data in Base64 format.
    """
    # Generate a 128-bit (16-byte) random key for Blowfish encryption
    key = get_random_bytes(16)
    
    # Create a new Blowfish cipher in CFB mode
    cipher = Blowfish.new(key, Blowfish.MODE_CFB)
    
    # Retrieve the initialization vector (IV) for the cipher
    iv = cipher.iv
    
    # Convert the user input to bytes
    input_bytes = user_input.encode('utf-8')
    
    # Encrypt the input string
    encrypted_bytes = cipher.encrypt(input_bytes)
    
    # Convert the encrypted data to Base64 format for easy display
    encrypted_base64 = b64encode(encrypted_bytes).decode('utf-8')
    
    # Print the results
    print("Initialization Vector (Base64):", b64encode(iv).decode('utf-8'))
    print("Encrypted Data (Base64):", encrypted_base64)
    
    # Return the key, IV, and encrypted data
    return key, iv, encrypted_base64

def decrypt_blowfish(key, iv, encrypted_data):
    """
    Decrypts an encrypted string using Blowfish encryption.
    
    Args:
    - key (bytes): The encryption key.
    - iv (bytes): The initialization vector used during encryption.
    - encrypted_data (str): The encrypted data in Base64 format.
    
    Returns:
    - decrypted_data (str): The decrypted plaintext string.
    """
    # Decode the Base64-encoded encrypted data back to bytes
    encrypted_bytes = b64decode(encrypted_data)
    
    # Create a new Blowfish cipher for decryption using the same key and IV
    cipher = Blowfish.new(key, Blowfish.MODE_CFB, iv=iv)
    
    # Decrypt the encrypted data
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    
    # Convert the decrypted bytes back to a string
    decrypted_data = decrypted_bytes.decode('utf-8')
    
    # Print the result
    print("Decrypted Data:", decrypted_data)
    
    return decrypted_data

if __name__ == "__main__":
    # Get user input
    user_input = input("Enter the string to encrypt: ")
    
    # Encrypt the user input and retrieve key, IV, and encrypted data
    key, iv, encrypted_data = encrypt_blowfish(user_input)
    
    # Decrypt the encrypted data
    decrypt_blowfish(key, iv, encrypted_data)
