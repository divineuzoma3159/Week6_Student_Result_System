import unittest
from grading import calculate_grade

class TestGrading(unittest.TestCase):
    def test_grade_a_boundary(self):
        self.assertEqual(calculate_grade(70), "A")
    def test_grade_b_boundary(self):
        self.assertEqual(calculate_grade(60), "B")
    def test_grade_f(self):
        
        
        self.assertEqual(calculate_grade(0), "F")
    def test_invalid_high_score(self):
        with self.assertRaises(ValueError):
            calculate_grade(101)
    def test_below_minimum(self):
        with self.assertRaises(ValueError):
            calculate_grade(-1)
    def test_maximum_score(self):
        self.assertEqual(calculate_grade(100), "A")
    def test_just_below_maximum_score(self):
        self.assertEqual(calculate_grade(99), "A")
    def test_minimum_score(self):
        self.assertEqual(calculate_grade(1), "F")
    # Tests grade transitions
    def test_grade_transition(self):
        self.assertEqual(calculate_grade(39), "F")
        self.assertEqual(calculate_grade(40), "E")
        self.assertEqual(calculate_grade(44), "E")
        self.assertEqual(calculate_grade(45), "D")
        self.assertEqual(calculate_grade(49), "D")
        self.assertEqual(calculate_grade(50), "C")
        self.assertEqual(calculate_grade(59), "C")
        self.assertEqual(calculate_grade(60), "B")
        self.assertEqual(calculate_grade(69), "B")
        self.assertEqual(calculate_grade(70), "A")
        
if __name__ == "__main__":
    unittest.main()
