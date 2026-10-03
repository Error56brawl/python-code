def caesar_cipher(text, shift,my_dict):
    result = ""

    for ch in text:
        if ch.isupper():
            c = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            my_dict[ch] = c
            result += c

        elif ch.islower():
            d = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            my_dict[ch] = d
            result += d

        else:
            result += ch

    print(my_dict)
    return result


text = input("Enter text: ")
shift = int(input("Enter shift: "))
my_dict={}
encrypted = caesar_cipher(text, shift,my_dict)
print("Encrypted text:", encrypted)

decrypted = caesar_cipher(encrypted, -shift,my_dict)
print("Decrypted text:", decrypted)