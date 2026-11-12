"""Unit tests for totals, result records, GPA and input validation."""
import unittest
from result_module import calculate_total_score, generate_result, calculate_gpa


class TestResultModule(unittest.TestCase):
    def test_total_score(self):
        self.assertEqual(calculate_total_score(18, 17, 52), 87)

    def test_generated_result(self):
        result = generate_result(" John ", " CSC/2026/001 ", "SWE 306", 18, 17, 52)
        self.assertEqual(result["student_name"], "John")
        self.assertEqual(result["registration_number"], "CSC/2026/001")
        self.assertEqual(result["total"], 87)
        self.assertEqual(result["grade"], "A")
        self.assertEqual(result["grade_point"], 5)

    def test_score_limits(self):
        self.assertEqual(calculate_total_score(0, 0, 0), 0)
        self.assertEqual(calculate_total_score(20, 20, 60), 100)
        for scores in [(-1, 10, 30), (21, 10, 30), (10, 21, 30), (10, 10, 61)]:
            with self.subTest(scores=scores):
                with self.assertRaises(ValueError):
                    calculate_total_score(*scores)

    def test_score_type_validation(self):
        with self.assertRaises(TypeError):
            calculate_total_score("18", 17, 52)
        with self.assertRaises(TypeError):
            calculate_total_score(True, 17, 52)

    def test_student_validation(self):
        with self.assertRaises(ValueError):
            generate_result("  ", "CSC/2026/001", "SWE 306", 18, 17, 52)
        with self.assertRaises(ValueError):
            generate_result("John", " ", "SWE 306", 18, 17, 52)

    def test_weighted_gpa(self):
        courses = [
            {"grade_point": 5, "credit_unit": 3},
            {"grade_point": 4, "credit_unit": 2},
            {"grade_point": 3, "credit_unit": 3},
        ]
        self.assertEqual(calculate_gpa(courses), 4.0)

    def test_gpa_validation(self):
        with self.assertRaises(ValueError):
            calculate_gpa([])
        with self.assertRaises(ValueError):
            calculate_gpa([{"grade_point": 6, "credit_unit": 2}])
        with self.assertRaises(ValueError):
            calculate_gpa([{"grade_point": 4, "credit_unit": 0}])


if __name__ == "__main__":
    unittest.main()
