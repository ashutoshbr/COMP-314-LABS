import unittest
from main import dynamic_kp


class KnapsackTest(unittest.TestCase):
    def test_dynamic_kp(self):
        expected_output = 1400
        acutal_output = dynamic_kp([800, 600, 300, 250], [3, 2, 1, 5], 5)
        self.assertEqual(acutal_output, expected_output)


if __name__ == "__main__":
    unittest.main()
