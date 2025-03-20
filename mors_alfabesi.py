from encryption import encrypt_text
from decryption import decrypt_text


def main():
    # Mors sözlüğü
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', 'Ö': '---.', 'Ü': '..--', 'Ç': '----', 'Ş': '...-.', 
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': ' '
    }

    while(True):
        print("\n Morse Kodu Uygulaması")
        print("1 - Şifreleme (Düz metni Morse koduna çevirin)")
        print("2 - Şifre Çözme (Morse Kodunu düz metne çevirin)")
        print("3 - Çıkış")

        choice = input("Seçiminizi Yapın: ")

        if choice == '1':
            text = input("Şifrelenecek Metin: ")
            print(encrypt_text(text.upper(),morse_dict))
        elif choice == '2':
            text = input('Çözümlenecek Morse kodu girin: ')
            print(decrypt_text(text.upper(), morse_dict))
        elif choice == '3':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()