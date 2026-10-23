def get_valid_score(prompt):
    """Helper function to validate user score inputs."""
    while True:
        try:
            score = float(input(prompt))
            if 0 <= score <= 100:
                return score
            print("Invalid input! Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical score.")

def calculate_grade():
    print("==============================================")
    print("   STUDENT GRADE CALCULATOR & GPA CONVERTER   ")
    print("==============================================")
    
    # Prompting with built-in validation
    quiz_score = get_valid_score("Enter Quiz score (0-100): ")
    exam_score = get_valid_score("Enter Exam score (0-100): ")
    project_score = get_valid_score("Enter Project score (0-100): ")

    # Weighted calculation (30% Quizzes, 50% Exams, 20% Projects)
    final_grade = (quiz_score * 0.30) + (exam_score * 0.50) + (project_score * 0.20)

    # Determine letter grade, GPA, and status
    if final_grade >= 90:
        letter, gpa = "A", 4.0
    elif final_grade >= 80:
        letter, gpa = "B", 3.0
    elif final_grade >= 70:
        letter, gpa = "C", 2.0
    elif final_grade >= 60:
        letter, gpa = "D", 1.0
    else:
        letter, gpa = "F", 0.0

    status = "PASSED" if final_grade >= 60 else "FAILED"

    print("\n================ FINAL REPORT ================")
    print(f"  Quiz Score (30%)    : {quiz_score:.2f}")
    print(f"  Exam Score (50%)    : {exam_score:.2f}")
    print(f"  Project Score (20%) : {project_score:.2f}")
    print("----------------------------------------------")
    print(f"  Final Weighted Score: {final_grade:.2f}%")
    print(f"  Letter Grade        : {letter}")
    print(f"  GPA Equivalent      : {gpa}")
    print(f"  Status              : {status}")
    print("==============================================\n")

if __name__ == "__main__":
    calculate_grade()