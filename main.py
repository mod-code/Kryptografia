import cipher_Morse
import cipher_CK

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from random import randint, choice
import string


# KLASY OKIEN

class WindowMenu(Screen):
	pass

class WindowMorse(Screen):
	c_input = ObjectProperty(None)
	c_output = ObjectProperty(None)
	err_msg = ObjectProperty(None)

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

class WindowManager(ScreenManager):
	pass

# Wczytanie pliku interfejsu (w języku kv)
kv = Builder.load_file("ui.kv")


class KryptografiaApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	KryptografiaApp().run()
