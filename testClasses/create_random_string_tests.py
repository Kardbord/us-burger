import string
import unittest

from utility.create_random_string import create_random_string


class CreateRandomStringTests(unittest.TestCase):
    def test_create_random_string_no_input(self):
        output = create_random_string()
        self.assertIsNot(output, None)
        self.assertIsNot(output, '')
        self.assertEqual(5, len(output))

    def test_create_random_string_didgit_weight_input(self):
        output = create_random_string(digit_weight=100)
        self.assertIsNot(output, None)
        self.assertIsNot(output, '')
        self.assertEqual(5, len(output))
        for character in output:
            self.assertTrue(character in string.digits)

        output = create_random_string(digit_weight=0)
        self.assertIsNot(output, None)
        self.assertIsNot(output, '')
        self.assertEqual(5, len(output))
        for character in output:
            self.assertFalse(character in string.digits)

        output = create_random_string(digit_weight=-10)
        self.assertIsNot(output, None)
        self.assertIsNot(output, '')
        self.assertEqual(5, len(output))
        for character in output:
            self.assertFalse(character in string.digits)

    def test_create_random_string_string_length_input(self):
        output = create_random_string(string_length=20)
        self.assertIsNot(output, None)
        self.assertIsNot(output, '')
        self.assertEqual(20, len(output))

        output = create_random_string(string_length=0)
        self.assertIsNot(output, None)
        self.assertEqual(output, '')

    def test_create_random_string_didgit_weight_and_string_length_input(self):
        output = create_random_string(digit_weight=100, string_length=20)
        self.assertIsNot(output, None)
        self.assertIsNot(output, '')
        self.assertEqual(20, len(output))
        for character in output:
            self.assertTrue(character in string.digits)

        output = create_random_string(digit_weight=0, string_length=-10)
        self.assertIsNot(output, None)
        self.assertEqual(output, '')


if __name__ == '__main__':
    unittest.main()
