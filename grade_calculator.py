def calculate_grade():
    print("=== Simple Grade Calculator & GPA Converter ===")
    
    try:
        # Get user inputs for weights and scores
        quiz_score = float(input("Enter your Quiz score (out of 100): "))
        exam_score = float(input("Enter your Exam score (out of 100): "))
        project_score = float(input("Enter your Project score (out of 100): "))

        # Calculate weighted average (Quizzes: 30%, Exams: 50%, Projects: 20%)
        final_grade = (quiz_score * 0.30) + (exam_score * 0.50) + (project_score * 0.20)

        # Determine letter grade
        if final_grade >= 90:
            letter = "A"
            gpa = 4.0
        elif final_grade >= 80:
            letter = "B"
            gpa = 3.0
        elif final_grade >= 70:
            letter = "C"
            gpa = 2.0
        elif final_grade >= 60:
            letter = "D"
            gpa = 1.0
        else:
            letter = "F"
            gpa = 0.0

        print("\n--- Results ---")
        print(f"Final Weighted Score: {final_grade:.2f}%")
        print(f"Letter Grade: {letter}")
        print(f"Equivalent GPA: {gpa}")
        
    except ValueError:
        print("Error: Please enter valid numbers only.")

if __name__ == "__main__":
    calculate_grade()