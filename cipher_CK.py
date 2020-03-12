# SZYFR CEZARA - KLASYCZNY

class CK:
	def __init__(self):
		pass


	@staticmethod
	def encrypt(words, key):
		encryptedMessage = ''

		try:
			key = int(key)
		except ValueError:
			key_value = 0
			for key_char in key:
				key_value += ord(key_char)
			key = key_value

		special = {' ', ',', '.', '?', '!', '/', '-', '(', ')', '#'}

		for char in words:
			if char not in special:  # jeśli znak nie jest znakiem specjalnym
				x = ord(char) + key
				if 65 <= ord(char) <= 90:  # znak to wielka litera
					while x < 65:
						x += 26     # zwiększ o zakrez liter
					while x > 90:
						x -= 26     # zmniejsz o zakrez liter
				elif 97 <= ord(char) <= 122:  # znak to mała litera
					while x < 97:
						x += 26     # zwiększ o zakrez liter
					while x > 122:
						x -= 26     # zmniejsz o zakrez liter

				encryptedMessage += chr(x)

			elif char == ' ':
				encryptedMessage += ' '
			elif char == ',':
				encryptedMessage += ','
			elif char == '.':
				encryptedMessage += '.'
			elif char == '?':
				encryptedMessage += '?'
			elif char == '!':
				encryptedMessage += '!'
			elif char == '/':
				encryptedMessage += '/'
			elif char == '-':
				encryptedMessage += '-'
			elif char == '(':
				encryptedMessage += '('
			elif char == ')':
				encryptedMessage += ')'
			elif char == '#':
				encryptedMessage += '#'

		return encryptedMessage

	@classmethod
	def decrypt(cls, words, key):
		try:
			key = int(key)
		except NameError:
			key = ord(key)
		except ValueError:
			key = ord(key)

		return cls.encrypt(words, - key)