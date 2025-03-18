""" Kullanicinin girdiği metni morse sözlüğünün içindeki şifreyle eşleştirip birleştiriyor.
    Eğer karakter sözlükte bulunmaz ise soru işareti eklenir.
"""
def encrypt_text(text, morse_dict):
    return ' '.join(morse_dict.get(char, '?') for char in text)