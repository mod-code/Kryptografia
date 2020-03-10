from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class OknoMenu(Screen):
	pass

class OknoSzyfrMor(Screen):
	pass

class OknoSzyfrCK(Screen):
	pass

class WindowManager(ScreenManager):
	pass

kv = Builder.load_file("ui.kv")


class KryptografiaApp(App):
	def build(self):
		return kv


if __name__ == "__main__":
	KryptografiaApp().run()
