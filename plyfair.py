SIZE = 5

def generate_key_table(key):
    key_table = [['' for _ in range(SIZE)] for _ in range(SIZE)]
    dict_ = [0] * 26
    k, l = 0, 0

    for char in key:
        if char != 'j' and not dict_[ord(char) - ord('a')]:
            key_table[k][l] = char
            dict_[ord(char) - ord('a')] = 1
            l += 1
            if l == SIZE:
                k += 1
                l = 0

    for i in range(26):
        if not dict_[i] and i != ord('j') - ord('a'):
            key_table[k][l] = chr(i + ord('a'))
            l += 1
            if l == SIZE:
                k += 1
                l = 0

    return key_table

def search(key_table, a, b):
    if a == 'j': a = 'i'
    if b == 'j': b = 'i'
    pos = [0] * 4

    for i in range(SIZE):
        for j in range(SIZE):
            if key_table[i][j] == a:
                pos[0], pos[1] = i, j
            elif key_table[i][j] == b:
                pos[2], pos[3] = i, j
    return pos

def encrypt(text, key_table):
    encrypted = list(text)
    for i in range(0, len(encrypted), 2):
        pos = search(key_table, encrypted[i], encrypted[i + 1])
        if pos[0] == pos[2]:
            encrypted[i] = key_table[pos[0]][(pos[1] + 1) % SIZE]
            encrypted[i + 1] = key_table[pos[2]][(pos[3] + 1) % SIZE]
        elif pos[1] == pos[3]:
            encrypted[i] = key_table[(pos[0] + 1) % SIZE][pos[1]]
            encrypted[i + 1] = key_table[(pos[2] + 1) % SIZE][pos[3]]
        else:
            encrypted[i] = key_table[pos[0]][pos[3]]
            encrypted[i + 1] = key_table[pos[2]][pos[1]]
    return ''.join(encrypted)

def decrypt(text, key_table):
    decrypted = list(text)
    for i in range(0, len(decrypted), 2):
        pos = search(key_table, decrypted[i], decrypted[i + 1])
        if pos[0] == pos[2]:
            decrypted[i] = key_table[pos[0]][(pos[1] + SIZE - 1) % SIZE]
            decrypted[i + 1] = key_table[pos[2]][(pos[3] + SIZE - 1) % SIZE]
        elif pos[1] == pos[3]:
            decrypted[i] = key_table[(pos[0] + SIZE - 1) % SIZE][pos[1]]
            decrypted[i + 1] = key_table[(pos[2] + SIZE - 1) % SIZE][pos[3]]
        else:
            decrypted[i] = key_table[pos[0]][pos[3]]
            decrypted[i + 1] = key_table[pos[2]][pos[1]]
    return ''.join(decrypted)

def main():
    key = input("Enter the key (in lowercase, without 'j'): ").strip()
    key_table = generate_key_table(key)

    print("Key Table:")
    for row in key_table:
        print(' '.join(row))

    text = input("Enter the message to encrypt/decrypt (in lowercase, without 'j'): ").strip()
    if len(text) % 2 != 0:
        text += 'x'

    encrypted_message = encrypt(text, key_table)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, key_table)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()