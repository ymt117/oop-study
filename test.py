import unittest
import point

class TestPoint(unittest.TestCase):
    def point_test(self):
        p = Point(0.0, 0.0)
        self.assertEqual(0.0, p.get_x())
        self.assertEqual(0.0, p.get_y())

if __name__ == "__main__":
    unittest.main()