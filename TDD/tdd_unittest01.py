import unittest

word = input('input word: ')

class LowerUpperTestCode(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(word.lower(), word)

    def test_upper(self):
        self.assertEqual(word.upper(), word)

    def test_islower(self):
        self.assertTrue(word.islower())

    def test_split(self):
        text = 'work n study'
        self.assertEqual(text.split(), ['work', 'n', 'study'])
        with self.assertRaises(TypeError):
            text.split(3)

if __name__ == '__main__':
    unittest.main()
