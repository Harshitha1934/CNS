from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
def des_encrypt_decrypt_example():
   key = get_random_bytes(8)  # Generate a random 8-byte key
   cipher = DES.new(key, DES.MODE_CBC)
   plaintext = b"This is a secret message"
   padded_plaintext = pad(plaintext, DES.block_size)
   ciphertext = cipher.encrypt(padded_plaintext)
   print(f"Ciphertext (hex): {ciphertext.hex()}")

   decipher = DES.new(key, DES.MODE_CBC, cipher.iv)  # Need to use the same IV
   decrypted_padded_plaintext = decipher.decrypt(ciphertext)
   decrypted_plaintext = unpad(decrypted_padded_plaintext, DES.block_size)
   print(f"Decrypted Plaintext: {decrypted_plaintext.decode()}")
   
des_encrypt_decrypt_example()