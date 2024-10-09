def encrypt(text, shift):
    result = ""

    # Melakukan iterasi melalui setiap karakter dalam teks
    for i in range(len(text)):
        char = text[i]

        # Mengenkripsi huruf besar (A-Z)
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Mengenkripsi huruf kecil (a-z)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)

        # Jika karakter bukan huruf, biarkan tidak berubah
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)


# Contoh penggunaan
text = "aku"
shift = 3

# Teks terenkripsi
encrypted_text = encrypt(text, shift)
print("Teks terenkripsi:", encrypted_text)

# Teks terdekripsi
decrypted_text = decrypt(encrypted_text, shift)
print("Teks terdekripsi:", decrypted_text)
