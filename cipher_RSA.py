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
        phi_n = (self.p - 1) * (self.q - 1)

        e = random.randrange(1, phi_n)

        gcd_checker = GcdChecker(e, phi_n)
        coprime = gcd_checker.check_numbers()
        while coprime != 1:
            e = random.randrange(1, phi_n)
            gcd_checker.set_numbers(e, phi_n)
            coprime = gcd_checker.check_numbers()

        EEAchecker = EEA(e, phi_n)
        d = EEAchecker.odwr_mod()

        return (e, n), (d, n)


