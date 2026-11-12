from validation import validate_student, validate_score
from grading import calculate_grade, calculate_grade_point

def calculate_total_score(assignment, test, examination):
    # It validates assesment scores and returns thier sum
    validate_score(assignment, 20, "Assignment")
    validate_score(test, 20, "Test")
    validate_score(examination, 60, "Examination")
    return assignment + test + examination

def generate_result(name, registration_number, course_code,assignment, test, examination):
    validate_student(name, registration_number)
    total = calculate_total_score(assignment, test, examination)
    return {
        "student_name": name.strip(),
        "registration_number": registration_number.strip(),
        "course_code": course_code,
        "total": total,
        "grade": calculate_grade(total),
        "grade_point": calculate_grade_point(total)
    }
def calculate_gpa(course_results):
    if not course_results:
        raise ValueError("At least one course result is required")    
    weighted_points = 0
    total_units = 0
    for course in course_results:
        grade_point = course["grade_point"]
        credit_unit = course["credit_unit"]
        if not 0 <= grade_point <= 5:
            raise ValueError("Grade point must be between 0 and 5")
        if credit_unit <= 0:
            raise ValueError("Credit unit must be positive")
        weighted_points += grade_point * credit_unit 
        total_units += credit_unit
    return weighted_points / total_units

