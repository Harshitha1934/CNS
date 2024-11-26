# Euclidean Algorithm to find the Greatest Common Divisor (GCD)
def gcd(a, b):
    """
    Computes the GCD of two numbers using the Euclidean algorithm.
    Args:
    - a (int): First number.
    - b (int): Second number.
    Returns:
    - int: GCD of a and b.
    """
    if a == 0:
        return b
    return gcd(b % a, a)

# Driver code to test the Euclidean algorithm
print("Euclidean Algorithm:")
pairs = [(10, 15), (10, 35), (31, 2)]  # Test cases
for a, b in pairs:
    print(f"GCD({a}, {b}) = {gcd(a, b)}")


# Extended Euclidean Algorithm
def gcd_extended(a, b):
    """
    Computes the GCD of two numbers and also finds integers x and y such that:
    a * x + b * y = gcd(a, b)
    Args:
    - a (int): First number.
    - b (int): Second number.
    Returns:
    - tuple: (GCD of a and b, x, y)
    """
    if a == 0:
        return b, 0, 1  # Base case: gcd is b, coefficients are (0, 1)

    gcd, x1, y1 = gcd_extended(b % a, a)  # Recursive call
    x = y1 - (b // a) * x1  # Update x using the results of recursion
    y = x1  # Update y

    return gcd, x, y


