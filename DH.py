import random

# Function to perform modular exponentiation
def mod_exp(base, exp, mod):
    result = 1
    base = base % mod  # Ensure base is within the modulo range
    while exp > 0:
        if exp % 2 == 1:  # If exp is odd, multiply base with result
            result = (result * base) % mod
        exp = exp // 2  # Integer division by 2
        base = (base * base) % mod
    return result

# Diffie-Hellman parameters
p = 23  # Prime number
g = 5   # Primitive root modulo p

# Generate random private keys for Alice and Bob
a = random.randint(1, p - 1)  # Alice's private key
b = random.randint(1, p - 1)  # Bob's private key

# Compute public keys
A = mod_exp(g, a, p)  # Alice's public key
B = mod_exp(g, b, p)  # Bob's public key

# Compute shared secrets
shared_secret_alice = mod_exp(B, a, p)  # Alice's calculation
shared_secret_bob = mod_exp(A, b, p)    # Bob's calculation

# Output results
print(f"Alice's Public Key (A): {A}")
print(f"Bob's Public Key (B): {B}")
print(f"Shared Secret (Alice's calculation): {shared_secret_alice}")
print(f"Shared Secret (Bob's calculation): {shared_secret_bob}")

# Check if the shared secrets match
if shared_secret_alice == shared_secret_bob:
    print(f"Shared Secret: {shared_secret_alice}")
else:
    print("Error: Shared secrets do not match!")