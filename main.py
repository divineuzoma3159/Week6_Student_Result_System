from result_module import generate_result, calculate_gpa
def main():
    result = generate_result(
        name="John",
        registration_number="CSC/2026/001",
        course_code="SWE 306",
        assignment=18,
        test=17,
        examination=52
    )
    print("STUDENT RESULT")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
        courses = [{
            "grade_point": 5, 
            "credit_unit": 3
            },{
                "grade_point": 4, 
                "credit_unit": 2
                },{
                    "grade_point": 3,
                    "credit_unit": 3
                    }]   
        print("GPA:", round(calculate_gpa(courses), 2))
if __name__ == "__main__":
    main()
