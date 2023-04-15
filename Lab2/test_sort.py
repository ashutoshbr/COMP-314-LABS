import unittest

from sort import insertion_sort


array = [56, 23, 68, 12, 99, 2, 15]
sorted_data = [2, 12, 15, 23, 56, 68, 99]


class TestInsertionSort(unittest.TestCase):
    def test_sorted(self):
        obtained = insertion_sort(array)
        expected = sorted_data
        self.assertEqual(obtained, expected)


if __name__ == "__main__":
    unittest.main()
