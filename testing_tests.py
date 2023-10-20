import unittest
import rectangle_sa

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(52, rectangle_sa.surface_area(3, 4, 2))


if __name__ == '__main__':
    unittest.main()