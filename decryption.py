"""
    Verilen Morse kodlarını düz metne çeviren fonksiyon.

    Parametreler:
    morse_code (str): Çözümlenecek Morse kodu dizisi (boşluklarla ayrılmış).
    morse_dict (dict): Harfleri Morse kodlarına eşleyen sözlük.

    Dönüş:
    str: Çözümlenmiş metin. Geçersiz kodlar '?' ile gösterilir.
"""
def decrypt_text(morse_code, morse_dict):
    # Morse kodu -> Harf dönüşümü için ters bir sözlük oluştur
    reverse_dict = {value: key for key, value in morse_dict.items()}
    decrypted_text = []

    for code in morse_code.split():
        decrypted_text.append(reverse_dict.get(code, '?'))

    return ''.join(decrypted_text)
