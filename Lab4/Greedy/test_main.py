import unittest
from main import Item, Knapsack


class KnapsackTest(unittest.TestCase):
    def test_max_value(self):
        items_input = [Item(2, 800), Item(0.5, 600), Item(0.4, 300), Item(10, 250)]
        max_weight = 3
        k1 = Knapsack()
        acutal_output = k1.max_value(items_input, max_weight)
        expected_output = 1702.5
        self.assertEqual(acutal_output, expected_output)


if __name__ == "__main__":
    unittest.main()
