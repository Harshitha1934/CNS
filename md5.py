import hashlib
def generate_md5(input_string):
    md5_hash = hashlib.md5()  # Create an MD5 hash object
    md5_hash.update(input_string.encode())  # Update hash with encoded input string
    return md5_hash.hexdigest()  # Return hexadecimal representation of the hash

if __name__ == "__main__":
    input_string = "Hello, World!"
    print("MD5 Hash:", generate_md5(input_string))
