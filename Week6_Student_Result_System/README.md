# Week 6: Student Result Processing System

## Overview

This Python project was created for the Level 3 Software Engineering **Week 6 Practical: High-Quality Routines (Writing, Reviewing, Refactoring)**. It validates student information and assessment scores, calculates totals and letter grades, and calculates GPA using course credit units.

## Project structure

```text
Week6_Student_Result_System/
├── main.py                # Run the sample application and print the result
├── validation.py          # Validate student identity and assessment scores
├── grading.py             # Letter-grade boundaries and grade-point calculations
├── result_module.py       # Total score, result record and weighted GPA
├── test_grading.py        # Unit tests and grade boundary-value tests
├── test_result_module.py  # Unit tests for scores, results and GPA
├── CODE_REVIEW.md         # Slide 16–18 review and refactoring explanation
└── README.md              # Setup and usage instructions
```

## Requirements and setup

- Python 3 (no third-party Python packages required).
- Keep all Python files in the same project folder.
- Open the project folder in VS Code or a terminal.
- Check that Python is installed with `python --version` (or `python3 --version` on some systems).

## Running the project

```bash
python main.py
```

Expected output:

```text
STUDENT RESULT
Student Name: John
Registration Number: CSC/2026/001
Course Code: SWE 306
Total: 87
Grade: A
Grade Point: 5
GPA: 4.0
```

The sample total is **18 + 17 + 52 = 87**. The GPA calculation is the credit-weighted average:

`GPA = (5×3 + 4×2 + 3×3) / (3 + 2 + 3) = 4.0`

## Grading policy

| Total score | Grade | Grade point |
| --- | --- | --- |
| 70–100 | A | 5 |
| 60–69 | B | 4 |
| 50–59 | C | 3 |
| 45–49 | D | 2 |
| 40–44 | E | 1 |
| 0–39 | F | 0 |

The practical uses this illustrative grading scale. Assessment limits are 20 for assignment, 20 for test, and 60 for examination.

## Running automated tests

Run all test files with:

```bash
python -m unittest -v
```

The tests verify:

- Grade transitions at 39/40, 44/45, 49/50, 59/60 and 69/70.
- Minimum and maximum valid grades, as well as invalid values -1 and 101.
- Valid totals, maximum assessment component scores and invalid inputs.
- Student information validation and generation of result records.
- Weighted GPA and rejection of invalid GPA inputs.

## Code review and refactoring

The original routine on slide 16 had problems including unclear names, mixed responsibilities, missing validation, an incomplete grading scale, and printing inside the calculation routine. See **[CODE_REVIEW.md](CODE_REVIEW.md)** for the seven code smells, the refactoring improvements and an explanation of the intentionally corrected grading behavior.

## Version control

Use Git to keep a meaningful history of your own work. For example, after reviewing the state of the project:

```bash
git status
git add .
git commit -m "Complete result processing, tests and documentation"
```

If the repository is not yet initialized, first run `git init`. Further changes should be committed separately with meaningful descriptions.
