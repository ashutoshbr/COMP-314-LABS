import unittest

from search import linear_search, binary_search


random_data = [56, 23, 68, 12, 99, 2, 15]
sorted_data = sorted(random_data)


class TestLinearSearch(unittest.TestCase):
    def test_found(self):
        to_find = 12
        obtained = linear_search(to_find, random_data)
        expected = 3
        self.assertEqual(obtained, expected)

    def test_not_found(self):
        to_find = 123
        obtained = linear_search(to_find, random_data)
        expected = None
        self.assertEqual(obtained, expected)


class TestBinarySearch(unittest.TestCase):
    def test_found(self):
        to_find = 12
        obtained = binary_search(to_find, sorted_data)
        expected = 1
        self.assertEqual(obtained, expected)

    def test_not_found(self):
        to_find = 123
        obtained = binary_search(to_find, sorted_data)
        expected = None
        self.assertEqual(obtained, expected)


if __name__ == "__main__":
    unittest.main()
