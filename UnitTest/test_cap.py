# unittest
import unittest  # they are modules
import cap


class TestCap(unittest.TestCase):
    def test_one_word(self):
        test = "python"
        t = cap.cap_text(test)
        self.assertEqual(t, "Python")  # assert t = ("Python")

    def test_two_word(self):
        self.assertEqual(cap.cap_text("python three"), "Python Three")

    def test_num(self):
        try:
            cap.cap_text(2)
        except:
            self.fail("your function should not produce error my darling!")
        # self.assertRaises(AttributeError, cap.cap_text,
        #                   2)  # exception thrown/raise


if (__name__ == "__main__"):
    unittest.main()
