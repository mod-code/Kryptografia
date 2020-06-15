from unittest import TestCase

from main import WindowMorse, WindowRSA, WindowCK, WindowCL
from cipher_Morse import Morse
from cipher_CK import CK
from cipher_CL import CL
from cipher_RSA import RSA

# ------------------------------------------------------------------------------------
#   FAIL TESTS

class TestWindowMorse(TestCase):
	def test_flash(self):
		self.fail()

	def test_mig_on(self):
		self.fail()

	def test_mig_off(self):
		self.fail()

	def test_error_mess(self):
		self.fail()

	def test_btn_input(self):
		self.fail()

	def test_btn_output(self):
		self.fail()


class TestWindowRSA(TestCase):
	def test_btn_genkey(self):
		self.fail()

	def test_btn_input(self):
		self.fail()

	def test_btn_output(self):
		self.fail()


class TestWindowCK(TestCase):
	def test_btn_genkey(self):
		self.fail()

	def test_btn_input(self):
		self.fail()

	def test_btn_output(self):
		self.fail()


class TestWindowCL(TestCase):
	def test_btn_genkey(self):
		self.fail()

	def test_btn_input(self):
		self.fail()

	def test_btn_output(self):
		self.fail()


class TestKryptografiaApp(TestCase):
	def test_build(self):
		self.fail()

# ------------------------------------------------------------------------------------
#   MORSE WINDOW TESTS // TESTY OKNA MORSE


class TestMorse(TestCase):
	def setUp(self):
		self.tMorse = WindowMorse()


class TestMorseErrorMessage(TestMorse):
	def test_no_error(self):
		self.assertEqual(self.tMorse.err_msg.text, "")

	def test_error_msg(self):
		self.tMorse.err_msg()
		self.assertEqual(self.tMorse.err_msg.text, "Wykryto nieoczekiwany znak specjalny!")

	def test_no_input_error(self):
		self.tMorse.btn_input()
		self.assertEqual(self.tMorse.err_msg.text, "Wykryto brak kodu lub nieoczekiwany znak specjalny!")


class TestMorseFlashing(TestMorse):
	def flash_on(self):
		self.tMorse.mig_on()
		self.assertEqual(self.tMorse.flashlight.background_color, (1, 1, 1, 1))

	def flash_off(self):
		self.tMorse.mig_off()
		self.assertEqual(self.tMorse.flashlight.background_color, (0, 0, 0, 1))


class TestMorseInputOutput(TestMorse):
	def empty_input_at_start(self):
		self.assertEqual(self.tMorse.c_input.text, "")

	def empty_output_at_start(self):
		self.assertEqual(self.tMorse.c_output.text, "")

# ------------------------------------------------------------------------------------
#   RSA WINDOW TESTS // TESTY OKNA RSA


class TestRSA(TestCase):
	def setUp(self):
		self.tRSA = WindowRSA()


class TestRSAInputOutput(TestRSA):
	def empty_input_at_start(self):
		self.assertEqual(self.tRSA.c_input.text, "")

	def empty_output_at_start(self):
		self.assertEqual(self.tRSA.c_output.text, "")


class TestRSAKeys(TestRSA):
	def empty_keys_at_start(self):
		self.assertEqual(self.tRSA.keyE.text, "")
		self.assertEqual(self.tRSA.keyD.text, "")
		self.assertEqual(self.tRSA.keyN.text, "")

	def key_generation(self):
		self.tRSA.btn_genkey()
		self.assertNotEqual(self.tRSA.keyE.text, "")
		self.assertNotEqual(self.tRSA.keyD.text, "")
		self.assertNotEqual(self.tRSA.keyN.text, "")

# ------------------------------------------------------------------------------------
#   CK WINDOW TESTS // TESTY OKNA CK (Cezara Klasyczny)


class TestCK(TestCase):
	def setUp(self):
		self.tCK = WindowCK()


class TestCKInputOutput(TestCK):
	def empty_input_at_start(self):
		self.assertEqual(self.tCK.c_input.text, "")

	def empty_output_at_start(self):
		self.assertEqual(self.tCK.c_output.text, "")


class TestCKKey(TestCK):
	def empty_key_at_start(self):
		self.assertEqual(self.tCK.key.text, "")

	def key_generation(self):
		self.tCK.btn_genkey()
		self.assertNotEqual(self.tCK.key.text, "")


# ------------------------------------------------------------------------------------
#   CL WINDOW TESTS // TESTY OKNA CL (Cezara Liczbowy)


class TestCL(TestCase):
	def setUp(self):
		self.tCL = WindowCL()


class TestCLInputOutput(TestCL):
	def empty_input_at_start(self):
		self.assertEqual(self.tCL.c_input.text, "")

	def empty_output_at_start(self):
		self.assertEqual(self.tCL.c_output.text, "")


class TestCLKey(TestCL):
	def empty_key_at_start(self):
		self.assertEqual(self.tCL.key.text, "")

	def key_generation(self):
		self.tCL.btn_genkey()
		self.assertNotEqual(self.tCL.key.text, "")


# ------------------------------------------------------------------------------------
#   cipher_Morse TESTS


class TestCipherMorse(TestCase):
	def setUp(self):
		self.Cip_Morse = Morse()


class TestCipherMorseEncrypt(TestCipherMorse):
	def encrypt_A(self):
		a = self.Cip_Morse.encrypt("A")
		self.assertEqual(a, ".- ")

	def encrypt_1(self):
		a = self.Cip_Morse.encrypt("1")
		self.assertEqual(a, ".---- ")


class TestCipherMorseDecrypt(TestCipherMorse):
	def decrypt_A(self):
		a = self.Cip_Morse.decrypt(".- ")
		self.assertEqual(a, "A")

	def decrypt_1(self):
		a = self.Cip_Morse.encrypt(".---- ")
		self.assertEqual(a, "1")


# ------------------------------------------------------------------------------------
#   cipher_CK TESTS


class TestCipherCK(TestCase):
	def setUp(self):
		self.Cip_CK = CK()


class TestCipherCKEncrypt(TestCipherCK):
	def encrypt_A_no_key(self):
		a = self.Cip_CK.encrypt("A", 0)
		self.assertEqual(a, "A")

	def encrypt_A_with_key(self):
		a = self.Cip_CK.encrypt("A", 1)
		self.assertEqual(a, "B")

	def encrypt_1_no_key(self):
		a = self.Cip_CK.encrypt("1", 0)
		self.assertEqual(a, "1")

	def encrypt_1_with_key(self):
		a = self.Cip_CK.encrypt("1", 1)
		self.assertEqual(a, "2")


class TestCipherCKDecrypt(TestCipherCK):
	def decrypt_A_no_key(self):
		a = self.Cip_CK.encrypt("A", 0)
		self.assertEqual(a, "65_")

	def decrypt_A_with_key(self):
		a = self.Cip_CK.encrypt("A", 1)
		self.assertEqual(a, "66_")

	def decrypt_1_no_key(self):
		a = self.Cip_CK.encrypt("1", 0)
		self.assertEqual(a, "49_")

	def decrypt_1_with_key(self):
		a = self.Cip_CK.encrypt("1", 1)
		self.assertEqual(a, "50_")
