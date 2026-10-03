def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))

        else:
            result += ch

    return result


text = input("Enter text: ")
shift = int(input("Enter shift: "))

encrypted = caesar_cipher(text, shift)
print("Encrypted text:", encrypted)

decrypted = caesar_cipher(encrypted, -shift)
print("Decrypted text:", decrypted)