import Crypto
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import base64

class TripleDES:
    def __init__(self, encryption_key):
        # Ensure the key length is 24 bytes for DESede (Triple DES)
        self.encryption_key = encryption_key.encode('utf-8')[:24].ljust(24, b'\0')  # Pad or truncate the key to 24 bytes
        self.cipher = DES3.new(self.encryption_key, DES3.MODE_ECB)  # Using ECB mode for simplicity

    def encrypt(self, plaintext):
        # Convert plaintext to bytes and pad it to a multiple of 8 bytes
        plaintext_bytes = plaintext.encode('utf-8')
        padded_text = pad(plaintext_bytes, DES3.block_size)  # DES block size is 8 bytes
        encrypted_bytes = self.cipher.encrypt(padded_text)  # Encrypt the padded plaintext
        # Encode the encrypted bytes to Base64 to make it readable
        return base64.b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(self, encrypted_text):
        # Decode the Base64 encoded ciphertext
        encrypted_bytes = base64.b64decode(encrypted_text)
        decrypted_padded_bytes = self.cipher.decrypt(encrypted_bytes)  # Decrypt the ciphertext
        # Remove padding and return the plaintext
        return unpad(decrypted_padded_bytes, DES3.block_size).decode('utf-8')

if __name__ == "__main__":
    # Input from the user
    string_to_encrypt = input("Enter the string: ")

    # Define encryption key
    encryption_key = "ThisIsSecretEncryptionKey"  # Must be 24 bytes for Triple DES
    des_encryptor = TripleDES(encryption_key)

    # Encrypt and decrypt the string
    encrypted = des_encryptor.encrypt(string_to_encrypt)
    decrypted = des_encryptor.decrypt(encrypted)

    # Output results
    print(f"\nString To Encrypt: {string_to_encrypt}")
    print(f"Encrypted Value: {encrypted}")
    print(f"Decrypted Value: {decrypted}")
