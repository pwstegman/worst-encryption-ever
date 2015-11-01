import unittest
from encrypt import encrypt

class TestEncrypt(unittest.TestCase):
    def test(self):
        self.assertEqual(encrypt("hi","abc"), 'haib')

if __name__ == '__main__':
    unittest.main()
