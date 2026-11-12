"""Unit tests for grading rules and boundary-value analysis."""
import unittest
from grading import calculate_grade, calculate_grade_point


class TestGrading(unittest.TestCase):
    def test_grade_boundaries(self):
        for score, expected_grade, expected_point in [
            (0, "F", 0), (1, "F", 0), (39, "F", 0), (40, "E", 1),
            (44, "E", 1), (45, "D", 2), (49, "D", 2), (50, "C", 3),
            (59, "C", 3), (60, "B", 4), (69, "B", 4), (70, "A", 5),
            (99, "A", 5), (100, "A", 5),
        ]:
            with self.subTest(score=score):
                self.assertEqual(calculate_grade(score), expected_grade)
                self.assertEqual(calculate_grade_point(score), expected_point)

    def test_out_of_range_scores(self):
        for score in [-1, 101]:
            with self.subTest(score=score):
                with self.assertRaises(ValueError):
                    calculate_grade(score)
                with self.assertRaises(ValueError):
                    calculate_grade_point(score)

    def test_invalid_types(self):
        for score in [True, "70", None]:
            with self.subTest(score=score):
                with self.assertRaises(TypeError):
                    calculate_grade(score)
                with self.assertRaises(TypeError):
                    calculate_grade_point(score)


if __name__ == "__main__":
    unittest.main()
