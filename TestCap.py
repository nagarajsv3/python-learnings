import unittest
import cap

class Testcap(unittest.TestCase):

    def test_one_word(self):
        inp = 'python'
        res = cap.cap_text(inp)
        self.assertEqual(res, 'Python')

    def test_multiple_words(self):
        inp = 'welcome to python'
        res = cap.cap_text(inp)
        self.assertEqual(res, 'Welcome To Python')

if __name__ == '__main__':
    unittest.main()
