def validate_student(name, registration_number):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name is required")
    if not isinstance(registration_number, str):
        raise TypeError("Registration number must be text")
    if not registration_number.strip():
        raise ValueError("Registration number is required")    
    return True
def validate_score(score, maximum, field_name):
    if not isinstance(score, (int, float)) or isinstance(score, bool):
        raise TypeError(f"{field_name} must be numeric")
    if not 0 <= score <= maximum:
        raise ValueError(f"{field_name} must be between 0 and {maximum}")
    return True
