import cipher_Morse
import cipher_CK
import cipher_CL
import cipher_RSA

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from random import randint, choice


# KLASY OKIEN
class WindowMenu(Screen):
	pass


class WindowMorse(Screen):
	c_input = ObjectProperty(None)
	c_output = ObjectProperty(None)
	err_msg = ObjectProperty(None)
	flashlight = ObjectProperty(None)

	def flash(self):
		self.err_msg.text = "Trwa miganie..."
		code = self.c_output.text
		t = 0
		for sym in code:
			if sym == '.':
				Clock.schedule_once(self.mig_on, t)
				t += 0.3
				Clock.schedule_once(self.mig_off, t)
				t += 0.3
			elif sym == '-':
				Clock.schedule_once(self.mig_on, t)
				t += 0.7
				Clock.schedule_once(self.mig_off, t)
				t += 0.3
			else:
				t += 0.3
		self.err_msg.text = ""

	def mig_on(self, *args):
		self.flashlight.background_color = (1, 1, 1, 1)

	def mig_off(self, *args):
		self.flashlight.background_color = (0, 0, 0, 1)


	def error_mess(self):
		self.err_msg.text = "Wykryto nieoczekiwany znak specjalny!"

	def btn_input(self):
		self.c_output.text = cipher_Morse.Morse.encrypt(self.c_input.text)
		if self.c_output.text == "":
			self.err_msg.text = "Wykryto brak kodu lub nieoczekiwany znak specjalny!"
		else:
			self.err_msg.text = ""

	def btn_output(self):
		self.c_input.text = cipher_Morse.Morse.decrypt(self.c_output.text)


class WindowRSA(Screen):
	c_input = ObjectProperty(None)
	c_output = ObjectProperty(None)
	keyE = ObjectProperty(None)
	keyD = ObjectProperty(None)
	keyN = ObjectProperty(None)
	err_msg = ObjectProperty(None)

	def btn_genkey(self):
		primes = [73, 79, 83, 89, 97, 101, 103, 107, 109]
		p = choice(primes)
		q = choice(primes)
		while p == q:
			p = choice(primes)
			q = choice(primes)
		rsa = cipher_RSA.RSA(p, q)
		rsa_keys = rsa.generate_keypair()
		self.keyE.text = str(rsa_keys[0])
		self.keyD.text = str(rsa_keys[1])
		self.keyN.text = str(rsa_keys[2])

	def btn_input(self):
		if self.keyE.text == "":
			self.err_msg.text = "Brak kluczy!"
		else:
			self.err_msg.text = ""
			rsa = cipher_RSA.RSA(89, 97)
			try:
				self.c_output.text = str(rsa.encrypt(int(self.keyE.text), int(self.keyN.text), str(self.c_input.text)))
			except AttributeError:
				self.err_msg.text = "ERROR!"

	def btn_output(self):
		if self.keyE.text == "":
			self.err_msg.text = "Brak kluczy!"
		else:
			self.err_msg.text = ""
			rsa = cipher_RSA.RSA(89, 97)
			try:
				fixed_message = self.c_output.text.strip('[]').split(", ")
				self.c_input.text = str(rsa.decrypt(int(self.keyD.text), int(self.keyN.text), fixed_message))
			except AttributeError:
				self.err_msg.text = "ERROR!"
			except ValueError:
				self.err_msg.text = "Brak wiadomości..."


class WindowCK(Screen):
	c_input = ObjectProperty(None)
	c_output = ObjectProperty(None)
	key = ObjectProperty(None)

	def btn_genkey(self):
		self.key.text = str(randint(1000, 9999))

	def btn_input(self):
		if self.key.text == "":
			self.key.text = "0"
		self.c_output.text = cipher_CK.CK.encrypt(self.c_input.text, self.key.text)

	def btn_output(self):
		if self.key.text == "":
			self.key.text = "0"
		self.c_input.text = cipher_CK.CK.decrypt(self.c_output.text, self.key.text)


class WindowCL(Screen):
	c_input = ObjectProperty(None)
	c_output = ObjectProperty(None)
	key = ObjectProperty(None)

	def btn_genkey(self):
		self.key.text = str(randint(1000, 9999))

	def btn_input(self):
		if self.key.text == "":
			self.key.text = "0"
		self.c_output.text = cipher_CL.CL.encrypt(self.c_input.text, self.key.text)

	def btn_output(self):
		if self.key.text == "":
			self.key.text = "0"
		self.c_input.text = cipher_CL.CL.decrypt(self.c_output.text, self.key.text)


class WindowManager(ScreenManager):
	pass

# Wczytanie pliku interfejsu (w języku kv)
kv = Builder.load_file("ui.kv")


class KryptografiaApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	KryptografiaApp().run()
