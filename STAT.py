import random
import math

def simple_columnar_transposition(message, key, num_rows, num_cols):
    # Pad the message with spaces if needed
    padded_message = message.ljust(num_rows * num_cols)  # Pad the message to fit the matrix
    # print(padded_message)
    matrix = []
    x = 0

    # Fill the matrix row by row
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append(padded_message[x])
            x += 1
        matrix.append(row)

    encrypted = []
    for i in key:
        for r in range(num_rows):
            if matrix[r][i] != " ":
                encrypted.append(matrix[r][i])  # No need for index correction since key starts from 0

    return ''.join(encrypted)

def advanced_columnar_transposition(message, key, num_rows, num_cols, rounds):
    transposed_message = message
    for _ in range(rounds):
        transposed_message = simple_columnar_transposition(transposed_message, key, num_rows, num_cols)
    return transposed_message

def generate_random_key(num_cols):
    key = list(range(num_cols))
    random.shuffle(key)
    # print(key)
    return key

def main():
    # Input message
    message = input("Enter the message: ").replace(" ", "")

    # Generate random rows and columns
    num_cols = random.randint(2, 10)  # Random number of columns between 2 and 10
    print("The random no of cols: ", num_cols)
    num_rows = math.ceil(len(message) / num_cols)
    print("The random no of rows: ", num_rows)
    # Generate a random key
    key = generate_random_key(num_cols)
    print("The randome key generated is: ", key)
    # Simple Columnar Transposition
    encrypted_message = simple_columnar_transposition(message, key, num_rows, num_cols)
    print(f"Simple Columnar Transposition: {encrypted_message}")

    # Advanced Columnar Transposition
    rounds = random.randint(1, 5)  # Random number of rounds between 1 and 5
    advanced_encrypted_message = advanced_columnar_transposition(message, key, num_rows, num_cols, rounds)
    print(f"Advanced Columnar Transposition (Rounds: {rounds}): {advanced_encrypted_message}")

if __name__ == "__main__":
    main()