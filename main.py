from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# KLASY OKIEN

class WindowMenu(Screen):
	pass

class WindowMorse(Screen):
	pass

class WindowCK(Screen):
	pass

class WindowManager(ScreenManager):
	pass

# Wczytanie pliku interfejsu (w języku kv)
kv = Builder.load_file("ui.kv")


class KryptografiaApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	KryptografiaApp().run()
