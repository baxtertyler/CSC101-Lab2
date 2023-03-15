# Lab 2 Test Cases
# Name: Tyler Baxter
# Section: 3
##############################################################
import unittest
import funcs


# 3 test cases for each function
class TestCases(unittest.TestCase):

    # This function tests if the math equation computes properly
    def test_do_math(self):
        self.assertEqual(funcs.do_math(0, 0), 0)
        self.assertEqual(funcs.do_math(1, 2), -7 / 24)
        self.assertAlmostEqual(funcs.do_math(2, 3), -34 / 44)

    # This function tests if the quadratic formula computes one root correctly
    def test_quadratic_formula1(self):
        self.assertEqual(funcs.quadratic_formula1(1, 2, -3), 1)
        self.assertEqual(funcs.quadratic_formula1(2, 2, -12), 2)
        self.assertEqual(funcs.quadratic_formula1(3, 6, -24), 2)

    # This function tests if the quadratic formula computes the other root correctly
    def test_quadratic_formula2(self):
        self.assertEqual(funcs.quadratic_formula2(1, 2, -3), -3)
        self.assertEqual(funcs.quadratic_formula2(2, 2, -12), -3)
        self.assertEqual(funcs.quadratic_formula2(3, 6, -24), -4)

    # This function tests if the manhattan distance is computed properly
    def test_distance(self):
        self.assertEqual(funcs.distance(0, 0, 4, 5), 9)
        self.assertEqual(funcs.distance(2, 3, 7, 12), 14)
        self.assertEqual(funcs.distance(12, 17, 1, 2), 26)

    # This function tests if the positive test is computed correctly
    def test_is_positive(self):
        self.assertTrue(funcs.is_positive(1))
        self.assertFalse(funcs.is_positive(-1))
        self.assertTrue(funcs.is_positive(100))

    # This function tests if the divisible by 7 is computed correctly
    def test_dividable_by_7(self):
        self.assertTrue(funcs.dividable_by_7(49))
        self.assertFalse(funcs.dividable_by_7(48))
        self.assertTrue(funcs.dividable_by_7(7))


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
