from encryption import encrypt_text

# Mors sözlüğü
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', 'Ö': '---.', 'Ü': '..--', 'Ç': '----', 'Ş': '...-.', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' '
}

def decrypt(mors_code):
    mors_code = mors_code.strip()
    morse_words = mors_code.split('  ')
    text = ""

    for morse_word in morse_words:
        morse_characters = morse_word.split(' ')
        word = ""
        for code in morse_characters:
            for key, value in morse_dict.items():
                if code == value:
                    word += key
        text += word + ' '

    return text.strip()

text = input("Şifrelenecek metni girin: ")
print("Morse Kodu:", encrypt_text(text.upper(), morse_dict))

# decoded_text = decrypt(mors_code)
# print("Çözülmüş Metin:", decoded_text)

# encrypted_text = input("Şifreli metni giriniz: ")
# original_text = decrypt(encrypted_text)
# print("Orjinal metin: ", original_text)
