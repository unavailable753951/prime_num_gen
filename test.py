import unittest
from module1 import PrimeGenerator
from module2 import save_list_to_file
import os

class TestPrimeGenerator(unittest.TestCase):
    def test_generate_primes(self):
        generator = PrimeGenerator(10, 50)
        primes = generator.generate_primes()
        expected_primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(primes, expected_primes)

class TestFileOperations(unittest.TestCase):
    def test_save_list_to_file(self):
        primes = [2, 3, 5, 7, 11, 13]
        filename = 'test_primes.txt'
        
        formats = {
            '1': '2, 3, 5, 7, 11, 13\n',
            '2': '2 3 5 7 11 13\n',
            '3': '2\n3\n5\n7\n11\n13\n',
            '4': '2,\n3,\n5,\n7,\n11,\n13,\n'
        }

        for format_choice, expected_content in formats.items():
            save_list_to_file(primes, filename, format_choice)
            with open(filename, 'r') as f:
                content = f.read()
                self.assertEqual(content, expected_content)
            os.remove(filename)

class TestConsoleInteraction(unittest.TestCase):
    def test_user_input(self):
        pass  # Możesz dodać testy dla interakcji z użytkownikiem, korzystając z biblioteki unittest.mock

if __name__ == '__main__':
    unittest.main()
