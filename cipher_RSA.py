import random


# Algorytm Euklidesa - odszukanie największego wspólnego dzielnika
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Algorytm sprawdzający czy liczba jest liczbą pierwszą
def isPrime(number):
    if number > 1:
        for i in range(2, number//2):
            if number % i == 0:
                return False
        else:
            return True
    else:
        return False

