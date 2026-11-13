# Code Review and Refactoring (Slides 16–18)

# Original routine (slide 16)

```python
def x(a, b, c, n):
    t = a + b + c
    if t >= 70:
        g = "A"
    elif t >= 60:
        g = "B"
    elif t >= 50:
        g = "C"
    else:
        g = "F"
    print(n, t, g)
    return t
```

# Seven identified code smells (slide 17)

1. **Unclear naming:** `x`, `a`, `b`, `c`, `n`, `t`, and `g` do not describe their purposes.
2. **Mixed responsibilities:** One function calculates the total, decides the grade, and prints the output.
3. **No input validation:** It does not check that scores are numeric or within the appropriate assessment limits.
4. **Incomplete grading scale:** It omits grades D and E required by the practical.
5. **Presentation coupled to calculation:** `print()` inside the calculation function makes the routine less reusable.
6. **No documentation:** There is no docstring or explicit explanation of invalid inputs.
7. **Harder to test independently:** The calculation, grading, and display are intertwined.

# Improvements that were made (slide 18)

- Replaced vague names with readable functions and variable names.
- Split student validation into `validation.py`, grading into `grading.py`, result and GPA processing into `result_module.py`, and display into `main.py`.
- Added type and range checks for student information and assessment scores.
- Centralized all six letter grades and their grade points in `GRADE_BOUNDARIES`.
- Kept printing in `main.py` instead of the calculation functions.
- Added docstrings to the revised main and result-processing routines.
- Added automated tests, including minimum/maximum scores and both sides of grade transitions.
- Fixed the early `return` in the GPA loop and the misplaced `main()` call in the uploaded code.

# Behavior comparison

For assessment scores of 18, 17, and 52, the total is **87** and grade is **A**, matching the original routine's grade at that total. The new module also returns grade point **5** and structured result data. For three sample courses of 3, 2, and 3 units with grade points 5, 4, and 3, the weighted GPA is **4.0**.

The original routine incorrectly assigns F to scores of 40–49. The updated system deliberately corrects that defect by assigning E to 40–44 and D to 45–49. This is a required behavior correction, not simply behavior-preserving refactoring.

# Verification

Run `python main.py` for the example and `python -m unittest -v` for the automated tests. Record the actual outputs and commit the final changes.
