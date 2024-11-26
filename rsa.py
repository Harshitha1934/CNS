def modcalci(m, e, N):
    """
    Function to calculate modular exponentiation.
    Computes (m^e) % N using a simple iterative method.
    """
    m1 = m
    for _ in range(e):
        c = m1 % N
        m1 = c * m
    return c


def modinv(a, m):
    """
    Function to calculate the modular inverse of `a` modulo `m`.
    Returns x such that (a * x) % m == 1.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Return None if no modular inverse is found


def gcd(x, y):
    """
    Function to calculate the greatest common divisor (GCD) of two numbers.
    Uses the Euclidean algorithm.
    """
    while y:
        x, y = y, x % y
    return x


def main():
    # RSA Key Creation
    p = int(input("Enter first prime: "))  # First prime number
    q = int(input("Enter second prime: "))  # Second prime number
    
    N = p * q  # Compute N (modulus)
    phi = (p - 1) * (q - 1)  # Euler's totient function
    e = 2  # Start with e = 2
    
    # Find e such that GCD(e, phi) = 1
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1
    
    # Public Key
    print(f"The public key (N, e) is: ({N}, {e})")
    
    # Get plaintext message from the user
    m = int(input("Enter the plaintext: "))
    
    # RSA Encryption
    c = modcalci(m, e, N)  # Encrypt message
    print(f"Encrypted message = {c}")
    
    # Private Key
    d = modinv(e, phi)  # Compute modular inverse of e
    print(f"The private key (N, d) is: ({N}, {d})")
    

# Run the program
main()
