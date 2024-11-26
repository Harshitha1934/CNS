from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def encrypt_blowfish(input_file, output_file):
    """
    Encrypts the content of a file using Blowfish encryption.
    
    Args:
    - input_file (str): Path to the input file to be encrypted.
    - output_file (str): Path to save the encrypted file.
    
    Returns:
    - key (bytes): The encryption key.
    - iv (bytes): The initialization vector used for encryption.
    """
    # Generate a 128-bit (16-byte) random key for Blowfish encryption
    key = get_random_bytes(16)
    
    # Create a new Blowfish cipher in CFB mode
    cipher = Blowfish.new(key, Blowfish.MODE_CFB)
    
    # Retrieve the initialization vector (IV) for the cipher
    iv = cipher.iv
    print("Initialization Vector of the Cipher:", b64encode(iv).decode('utf-8'))
    
    # Initialize variable to collect encrypted data for display
    encrypted_data = b""
    
    # Open the input file in binary read mode and output file in binary write mode
    with open(input_file, "rb") as fin, open(output_file, "wb") as fout:
        while True:
            # Read the input file in chunks of 64 bytes
            chunk = fin.read(64)
            if len(chunk) == 0:  # Stop when end of file is reached
                break
            # Encrypt the chunk
            encrypted_chunk = cipher.encrypt(chunk)
            # Write the encrypted chunk to the output file
            fout.write(encrypted_chunk)
            # Accumulate encrypted data for base64 display
            encrypted_data += encrypted_chunk
    
    # Display the encrypted data in Base64 format
    print("Encrypted Data (Base64):", b64encode(encrypted_data).decode('utf-8'))
    
    # Return the encryption key and initialization vector
    return key, iv

def decrypt_blowfish(key, iv, encrypted_file, decrypted_file):
    """
    Decrypts the content of a file encrypted using Blowfish encryption.
    
    Args:
    - key (bytes): The encryption key used during encryption.
    - iv (bytes): The initialization vector used during encryption.
    - encrypted_file (str): Path to the encrypted file.
    - decrypted_file (str): Path to save the decrypted file.
    """
    # Create a new Blowfish cipher for decryption using the same key and IV
    cipher = Blowfish.new(key, Blowfish.MODE_CFB, iv=iv)
    
    # Open the encrypted file in binary read mode and the output file in binary write mode
    with open(encrypted_file, "rb") as fin, open(decrypted_file, "wb") as fout:
        while True:
            # Read the encrypted file in chunks of 64 bytes
            chunk = fin.read(64)
            if len(chunk) == 0:  # Stop when end of file is reached
                break
            # Decrypt the chunk
            decrypted_chunk = cipher.decrypt(chunk)
            # Write the decrypted chunk to the output file
            fout.write(decrypted_chunk)
    
    print("Decryption complete. Check the decrypted file.")

if __name__ == "__main__":
    # Define file paths for the encryption and decryption process
    input_file = "inputFile.txt"
    encrypted_file = "outputFile.txt"
    decrypted_file = "decryptedFile.txt"
    
    # Encrypt the data and get the key and IV
    key, iv = encrypt_blowfish(input_file, encrypted_file)
    
    # Decrypt the data using the same key and IV
    decrypt_blowfish(key, iv, encrypted_file, decrypted_file)
