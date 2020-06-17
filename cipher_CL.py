# SZYFR CEZARA - LICZBOWY


class CL:
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

		# special = {' ', ',', '.', '?', '!', '/', '-', '(', ')', '#'}

		for char in words:
			if char == ' ':
				encryptedMessage += ' _'
			else:
				x = ord(char) + key
				"""
				if 10 <= ord(char) <= 99:  # tylko zakres liczby dwucyfrowych
					while x < 10:
						x += 90     # zwiększ o zakrez
					while x > 99:
						x -= 90     # zmniejsz o zakrez
						"""

				encryptedMessage += f'{x}_'

			"""
			elif char == ' ' and n == 0:
				encryptedMessage += ' '
			elif char == '_' and n == 1:
				encryptedMessage += ''
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
				"""

		return encryptedMessage

	@classmethod
	def decrypt(cls, words, key):
		encryptedMessage = ''

		try:
			key = int(key)
		except ValueError:
			key_value = 0
			for key_char in key:
				key_value += ord(key_char)
			key = key_value

		# special = {' ', ',', '.', '?', '!', '/', '-', '(', ')', '#'}
		words_n = words.split('_')
		print(words_n)
		for n in words_n:
			if n == ' ':
				encryptedMessage += ' '
			elif n == '':
				encryptedMessage += ''
			else:
				x = int(n) - key
				"""
				if not 10 <= x <= 99:  # tylko zakres liczby dwucyfrowych
					while x < 10:
						x += 90  # zwiększ o zakrez
					while x > 99:
						x -= 90  # zmniejsz o zakrez
						"""
				encryptedMessage += chr(x)

		return encryptedMessage
