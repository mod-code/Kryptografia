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


class RSA:
    def __init__(self):
        self.p = None
        self.q = None
