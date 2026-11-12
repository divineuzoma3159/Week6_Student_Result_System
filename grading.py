GRADE_BOUNDARIES = [
    (70, "A", 5),
    (60, "B", 4),
    (50, "C", 3),
    (45, "D", 2),
    (40, "E", 1),
    (0, "F", 0)
]

def calculate_grade(total_score):
    if not isinstance(total_score, (int, float)) or isinstance(total_score, bool):
        raise TypeError("Total score must be numeric")
    if not 0 <= total_score <= 100:
        raise ValueError("Total score must be between 0 and 100")
    for minimum, grade, points in GRADE_BOUNDARIES:
        if total_score >= minimum:
            return grade

def calculate_grade_point(total_score):
    if not isinstance(total_score, (int, float)) or isinstance(total_score, bool):
        raise TypeError("Total score must be numeric")
    if not 0 <= total_score <= 100:
        raise ValueError("Total score must be between 0 and 100")
    for minimum, grade, points in GRADE_BOUNDARIES:
        if total_score >= minimum:
            return points
