def main():
    students = []

    while True:
        print("\n--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_new_student(students)
            elif choice == "2":
                add_grades_for_student(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                find_top_performer(students)
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

        except Exception as e:
            print(f"An error occurred: {e}")


def add_new_student(students):
    """Add a new student to the list"""
    name = input("Enter student name: ").strip()

    # Check if student already exists
    for student in students:
        if student["name"].lower() == name.lower():
            print(f"Student '{name}' already exists!")
            return

    # Create new student dictionary
    new_student = {
        "name": name,
        "grades": []
    }
    students.append(new_student)
    print(f"Student '{name}' added successfully!")


def add_grades_for_student(students):
    """Add grades for an existing student"""
    if not students:
        print("No students available. Please add students first.")
        return

    name = input("Enter student name: ").strip()

    # Find the student
    student_found = None
    for student in students:
        if student["name"].lower() == name.lower():
            student_found = student
            break

    if not student_found:
        print(f"Student '{name}' not found!")
        return

    print(f"Adding grades for {student_found['name']}. Enter grades (0-100) or 'done' to finish:")

    while True:
        grade_input = input("Enter a grade (or 'done' to finish): ").strip()

        if grade_input.lower() == 'done':
            break

        try:
            grade = float(grade_input)
            if 0 <= grade <= 100:
                student_found["grades"].append(grade)
                print(f"Grade {grade} added successfully!")
            else:
                print("Invalid grade! Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a valid number or 'done'.")


def calculate_average(grades):
    """Calculate average of grades, handling empty list"""
    if not grades:
        return None
    return sum(grades) / len(grades)


def show_report(students):
    """Generate and display report for all students"""
    if not students:
        print("No students available.")
        return

    print("\n--- Student Report ---")

    averages = []

    for student in students:
        try:
            avg = calculate_average(student["grades"])
            if avg is None:
                print(f"{student['name']}'s average grade is N/A.")
            else:
                formatted_avg = round(avg, 1)
                print(f"{student['name']}'s average grade is {formatted_avg}.")
                averages.append(formatted_avg)
        except ZeroDivisionError:
            print(f"{student['name']}'s average grade is N/A.")
        except Exception as e:
            print(f"Error calculating average for {student['name']}: {e}")

    # Calculate overall statistics
    if averages:
        max_avg = max(averages)
        min_avg = min(averages)
        overall_avg = sum(averages) / len(averages)

        print("---")
        print(f"Max Average: {max_avg}")
        print(f"Min Average: {min_avg}")
        print(f"Overall Average: {overall_avg:.1f}")
    else:
        print("---")
        print("No grades available for statistics.")


def find_top_performer(students):

    if not students:
        print("No students available.")
        return

    # Filter students with valid grades
    students_with_grades = []
    for student in students:
        avg = calculate_average(student["grades"])
        if avg is not None:
            students_with_grades.append((student, avg))

    if not students_with_grades:
        print("No students with grades available.")
        return

    # Find top performer using max with lambda
    try:
        top_student, top_avg = max(students_with_grades, key=lambda x: x[1])
        print(f"Top performer: {top_student['name']} with average grade {top_avg:.1f}")
    except Exception as e:
        print(f"Error finding top performer: {e}")


if __name__ == "__main__":
    main()