import unittest

from is_prime import is_prime_v2 as is_prime  ####


class PrimeTest(unittest.TestCase):
    def test_is_prime_ok(self):
        for i in [2, 3, 5, 7, 11]:
            self.assertTrue(is_prime(i))

    def test_is_prime_no(self):
        for i in [1, 4, 6, 8, 9]:
            self.assertFalse(is_prime(i))

    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-1))

    def test_is_prime_string(self):
        with self.assertRaises(TypeError): ### type error 終了 specific error define
            is_prime('string')
