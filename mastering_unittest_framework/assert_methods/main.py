import unittest

def add(a, b):
    return a + b

def is_even(n):
    return n % 2 == 0

def get_item(lst, index):
    if index < 0 or index >= len(lst):
        return None
    return lst[index]

def make_none():
    return None

class TestFunctions(unittest.TestCase):
    # Write your test methods below using assertEqual, assertNotEqual, assertTrue, assertFalse, assertIs, assertIsNone, assertIn, and assertIsInstance
    pass

if __name__ == "__main__":
    unittest.main()

def test_add_equal
    self.assertEqual(add(2, 3), 5)

def test_add_not_equal
    self.assertNotEqual(add(2, 2), 5)

def test_is_even_true
    self.assetTrue(is_even(4))

def test_is_even_false 
