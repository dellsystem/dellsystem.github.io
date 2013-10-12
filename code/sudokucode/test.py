import unittest

import utils


class TestSudokuCoder(unittest.TestCase):
    def setUp(self):
        self.s = utils.SudokuCoder()

    def test_completeness(self):
        plaintext = 'thisisatest'
        ciphertext = self.s.encode(plaintext)
        result = self.s.decode(ciphertext)[:len(plaintext)]
        self.assertEqual(plaintext, result)


if __name__ == '__main__':
    unittest.main()
