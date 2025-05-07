import unittest
from os import name

from parentheses import countWellFormedParenthesis

class TestParentheses(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(countWellFormedParenthesis(1), 1)
        self.assertEqual(countWellFormedParenthesis(2), 2)
        self.assertEqual(countWellFormedParenthesis(3), 5)
        self.assertEqual(countWellFormedParenthesis(4), 14)
        self.assertEqual(countWellFormedParenthesis(5), 42)
        self.assertEqual(countWellFormedParenthesis(15), 9694845)

    def test_performance(self):
        import time
        start = time.time()
        result = countWellFormedParenthesis(15)
        duration = time.time() - start
        self.assertTrue(duration < 1.0)
        self.assertEqual(result, 9694845)

if name == '__main__':
    unittest.main()