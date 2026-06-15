import math
import unittest

from algoritma_araci.algorithms import (
    closest_pair_to_target,
    fibonacci,
    gcd,
    is_prime,
    kth_smallest_unique,
    matrix_multiply,
    min_value,
    parse_number_list,
    repeated_elements,
    sqrt_newton,
    word_frequency_from_text,
)


class TestAlgorithms(unittest.TestCase):
    def test_kth_smallest_unique(self):
        self.assertEqual(kth_smallest_unique([5, 1, 3, 3, 2], 3), 3)

    def test_closest_pair_to_target(self):
        pair = closest_pair_to_target([1, 4, 7, 10], 11)
        self.assertEqual(sum(pair), 11)

    def test_repeated_elements(self):
        self.assertEqual(repeated_elements([1, 2, 2, 3, 3, 3]), [2, 3])

    def test_matrix_multiply(self):
        matrix_a = [[1, 2, 3], [4, 5, 6]]
        matrix_b = [[7, 8], [9, 10], [11, 12]]
        self.assertEqual(matrix_multiply(matrix_a, matrix_b), [[58, 64], [139, 154]])

    def test_word_frequency_from_text(self):
        result = word_frequency_from_text("Elma, elma armut! Kiraz kiraz.")
        self.assertEqual(result["elma"], 2)
        self.assertEqual(result["armut"], 1)
        self.assertEqual(result["kiraz"], 2)

    def test_min_value(self):
        self.assertEqual(min_value([4, 2, 8, -1]), -1)

    def test_sqrt_newton(self):
        self.assertTrue(math.isclose(sqrt_newton(25), 5.0, rel_tol=1e-9))

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)

    def test_is_prime(self):
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(100))

    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_parse_number_list(self):
        self.assertEqual(parse_number_list("1, 2.5, -3"), [1.0, 2.5, -3.0])


if __name__ == "__main__":
    unittest.main()
