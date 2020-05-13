import math
import random


class GcdChecker:
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    # Sprawdzenie największego wspólnego dzielnika dwóch liczb - Algorytm Euklidesa
    def check_numbers(self):
        while self.secondNumber != 0:
            self.firstNumber, self.secondNumber = self.secondNumber, self.firstNumber % self.secondNumber
        return self.firstNumber

    def set_numbers(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber


class PrimeChecker:
    def __init__(self, number):
        self.number = number

    # Sprawdzenie czy podana liczba jest pierwsza
    def check_number(self):
        # Czy liczba jest dodatnia?
        if self.number > 1:
            # czy liczba jest parzysta i większa od 2?
            if self.number % 2 == 0 and self.number > 2:
                return False
            # sprawdzaj dzielnik do pierwiastka z liczb i co drugi krok (nie trzeba już parzystych sprawdzać)
            for i in range(3, int(math.sqrt(self.number)) + 1, 2):
                if self.number % i == 0:
                    return False
            return True
        else:
            return False

class EEA:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def calculate(self):
        p0, p1, a0, n0 = 0, 1, self.first_number, self.second_number
        q, r = n0 // a0, n0 % a0
        while r:
            t = p0 - q * p1
            if t >= 0:
                t = t % self.second_number
            else:
                t = self.second_number - ((-t) % self.second_number)
            p0, p1, n0, a0 = p1, t, a0, r
            q, r = n0 // a0, n0 % a0
        return p1


class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.character_dict = {
            'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19,
            'J': 20, 'K': 21, 'L': 22, 'M': 23, 'N': 24, 'O': 25, 'P': 26, 'Q': 27, 'R': 28,
            'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35, 'Z': 36, ' ': 37,
            'a': 38, 'b': 39, 'c': 40, 'd': 41, 'e': 42, 'f': 43, 'g': 44, 'h': 45, 'i': 46,
            'j': 47, 'k': 48, 'l': 49, 'm': 50, 'n': 51, 'o': 52, 'p': 53, 'q': 54, 'r': 55,
            's': 56, 't': 57, 'u': 58, 'v': 59, 'w': 60, 'x': 61, 'y': 62, 'z': 63, '.': 64,

        }

        self.inverted_character_dict = dict((value, key) for (key, value) in self.character_dict.items())

    def set_p_q(self, p, q):
        self.p = p
        self.q = q

    def generate_keypair(self):
        first_number_checker = PrimeChecker(self.p)
        second_number_checker = PrimeChecker(self.q)

        if not (first_number_checker.check_number() and second_number_checker.check_number()):
            raise ValueError('ERROR: Both numbers must be prime!')
        elif self.p == self.q:
            raise ValueError('ERROR: p and q cannot be equal!')

        n = self.p * self.q
        # Obliczenie funkcji Eulera
        phi_n = (self.p - 1) * (self.q - 1)

        # Losowo obliczany publiczny wykładnik e. Ma być on względnie pierwszy z funkcją Eulera
        e = random.randrange(1, phi_n)
        gcd_checker = GcdChecker(e, phi_n)
        coprime = gcd_checker.check_numbers()
        while coprime != 1:
            e = random.randrange(1, phi_n)
            gcd_checker.set_numbers(e, phi_n)
            coprime = gcd_checker.check_numbers()

        # Obliczany wykładnik prywatny, ma być odwrotnością modulo funkcji Eulera liczby e
        EEAchecker = EEA(e, phi_n)
        d = EEAchecker.calculate()

        # Pierwsza krotka to klucz publiczny, druga to klucz prywatny
        # return (e, n), (d, n)
        keys = (e, d, n)
        return keys

    def encrypt(self, e, n, message):
        # Każdy znak jest zamieniany według wzoru i wrzucany do listy
        message_numbers = []
        try:
            # Gdy wprowadzona wiadomość (znaki) nie mają odpowiednika w słowniku, przerwij i zwróć None
            for char in message:
                c = int(self.character_dict[char]) ** e % n
                message_numbers.append(c)
        except KeyError:
            print("ENCRYPTION ERROR: CHARACTER VALUE DOES NOT EXIST\n")
            # return None
        # Gdy wszystko się uda, zwróc liste z zakodowanymi znakami w postaci liczb
        return message_numbers

    def decrypt(self, d, n, encrypted_message):
        # Zabezpieczenie przed rozkodowywaniem pustej wiadomości
        if not encrypted_message:
            print("ENCRYPTED MESSAGE IS EMPTY!")
            return ""
        else:
            message_char_list = []
            # Odkodowywanie według wzoru
            for number in encrypted_message:
                c = int(number) ** d % n
                # Sprawdź czy odkodowana liczba jest w słowniku, jeśli nie przydziel randomowy znak
                try:
                    character = self.inverted_character_dict[c]
                except KeyError:
                    random_num = random.randrange(11, 37)
                    character = self.inverted_character_dict[random_num]
                message_char_list.append(character)
            # Zwróć wiadomość jako string
            return ''.join(message_char_list)


