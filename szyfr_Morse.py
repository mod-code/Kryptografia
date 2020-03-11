class Morse:
    def __init__(self):
        pass

    __MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                         'C': '-.-.', 'D': '-..', 'E': '.',
                         'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-',
                         'L': '.-..', 'M': '--', 'N': '-.',
                         'O': '---', 'P': '.--.', 'Q': '--.-',
                         'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--',
                         'X': '-..-', 'Y': '-.--', 'Z': '--..',
                         '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-',
                         '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-', 'Ą': '.-.-',
                         'Ć': '-.-..', 'Ę': '..-..', 'Ł': '.-..-',
                         'Ń': '--.--', 'Ó': '---.', 'Ś': '...-...',
                         'Ż': '--..-.', 'Ź': '--..-', ':': '---...'}

    __INVERSE_MORSE_DICT = dict((value, key) for (key, value) in __MORSE_CODE_DICT.items())

    @staticmethod
    def encrypt(words):

        mess = words.upper() # zabezpieczenie przed wprowadzeniem małych liter
        encryptedMessage = ''
        for char in mess:
            if char != ' ':  # jeśli znak nie jest spacją
                encryptedMessage += Morse.__MORSE_CODE_DICT[char] + ' '  # dodaj znak w kodzie morsa ze spacją
            else:
                encryptedMessage += ' '  # dodaj spację

        return encryptedMessage

    @staticmethod
    def decrypt(words):
        decypretMessage = ''
        buff = ''

        for char in words:

            if char != ' ':  # jeśli znak nie jest spacją
                spaces_counter = 0  # zmienna pomocnicza - reset licznika wystąpienia spacji
                buff += char  # zmienna pomocnicza przechowująca znak z Morsea

            else: # gdy znak to spacja
                spaces_counter += 1 # licznik zwiększany w celu zasygnalizowania nowego znaku

                if  spaces_counter == 2: # warunek sprawdzający czy nie wystąpiło nowe słowo
                    decypretMessage += ' ' # dodanie spacji do odzielenia słowa

                else:
                    decypretMessage += Morse.__INVERSE_MORSE_DICT[buff]
                    buff = '' # czyszczenie buffora znaków

        return decypretMessage

message = "WOJTEK JEST LEPSZY W PYTHONA NIŻ ODRZY :)"
print("Wiadomość przed zakodowaniem")
print(message)
print("")
print("Wiadomość po zakodowaniu")
encrypted_message = Morse.encrypt(message)
print(encrypted_message)
print("")
print("Wiadomość po odkodowaniu")
print(Morse.decrypt(encrypted_message))
