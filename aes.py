from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii

def as_hex(byte_array):
    """
    Converts a byte array to a hexadecimal string for easy representation.
    
    Args:
    - byte_array (bytes): The byte array to convert.
    
    Returns:
    - str: Hexadecimal string representation of the byte array.
    """
    return binascii.hexlify(byte_array).decode('utf-8')

def main():
    # Define the plaintext message to be encrypted
    message = "AES still rocks!!"
    print("Original Message:", message)

    # Generate a random 128-bit (16-byte) key for AES encryption
    key = get_random_bytes(16)  # 16 bytes = 128 bits
    print("Generated Key (Hex):", as_hex(key))

    # Initialize AES cipher in ECB (Electronic Codebook) mode for encryption
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt the message
    # - Convert the message to bytes using UTF-8 encoding
    # - Pad the message to be a multiple of the AES block size (16 bytes)
    encrypted = cipher.encrypt(pad(message.encode(), AES.block_size))
    print("Encrypted Message (Hex):", as_hex(encrypted))

    # Initialize AES cipher in ECB mode for decryption
    cipher_dec = AES.new(key, AES.MODE_ECB)

    # Decrypt the encrypted message
    # - Decrypt the encrypted bytes
    # - Unpad the decrypted message to get the original plaintext
    decrypted = unpad(cipher_dec.decrypt(encrypted), AES.block_size)
    original_string = decrypted.decode('utf-8')
    print("Decrypted Message:", original_string)
    print("Decrypted Message (Hex):", as_hex(decrypted))

if __name__ == "__main__":
    main()
