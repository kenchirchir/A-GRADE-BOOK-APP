import time
import json

class AddStudent:
    def __init__(self):
        self.student_list = []

    def add_student(self):
        students_name = input('Enter the student\'s name: ')
        students_email = input('Enter your email address: ')
        student_details = {'email': students_email, 'name': students_name, 'courses': [], 'grades': []}
        self.student_list.append(student_details)
        # Pause execution for 1 second
        time.sleep(1)
        print(f"Student {students_name} added successfully.")

class AddCourse:
    def __init__(self):
        self.course_list = []

    def add_course(self):
        course_name = input('Enter the course name that you want to register to: ')
        trimester = input('Enter your trimester: ')
        credits = int(input('Enter the course credits: '))
        course = {'course_name': course_name, 'trimester': trimester, 'credits': credits}
        self.course_list.append(course)
        # Pause execution for 1 second
        time.sleep(1)
        print(f"Course {course_name} added successfully.")

    def register_student_for_course(self, student_manager):
        student_name = input('Enter the student\'s name: ')
        course_name = input('Enter the course name to register for: ')
        #returns a value from an interator-(next) 
        student = next((s for s in student_manager.student_list if s['name'] == student_name), None
        if student:
            student['courses'].append(course_name)
            print(f"Student {student_name} registered for course {course_name} successfully.")
        else:
            print(f"Student {student_name} not found).")

grades_weight = {'tests': 50, 'quizzes': 30, 'assignment': 20}
students = {'Kenneth': (90, 80, 80), 'Freedy': (100, 75, 30)}

def initialize():
    print("Welcome to your grade book! Make a selection:")
    selection = int(input(
        "1: Add student\n"
        "2: Add course\n"
        "3: Register student for course\n"
        "4: Calculate GPA for student\n"
        "5: Search by GPA\n"
        "6: View grade\n"
        "7: Save data\n"
        "8: Load data\n"
        "9: exit\n"
    ))
    return selection

def calculate_GPA_for_student(student_manager):
    students_name = input('Enter the student\'s name: ')
    student = next((s for s in student_manager.student_list if s['name'] == students_name), None)
    if not student:
        print('Student not found.')
        return

    total_credits = 0
    total_points = 0
    for course in student['grades']:
        grade = course['grade']
        credits = course['credits']
        total_credits += credits
        total_points += grade * credits

    if total_credits == 0:
        print(f"Student {students_name} has no grades recorded.")
        return

    gpa = total_points / total_credits
    print(f"Student {students_name} has a GPA of {gpa:.2f}")

def search_by_GPA(student_manager):
    gpa_threshold = float(input('Enter the GPA threshold to search for: '))
    for student in student_manager.student_list:
        total_credits = 0
        total_points = 0
        for course in student['grades']:
            grade = course['grade']
            credits = course['credits']
            total_credits += credits
            total_points += grade * credits

        if total_credits > 0:
            gpa = total_points / total_credits
            if gpa >= gpa_threshold:
                print(f"Student {student['name']} has a GPA of {gpa:.2f}")

def view_grade(student_manager):
    students_name = input('Enter the student\'s name: ')
    student = next((s for s in student_manager.student_list if s['name'] == students_name), None)
    if not student:
        print('Student not found.')
        return

    test_score = int(input('Enter the student\'s test score (0-100): '))
    quiz_score = int(input('Enter the student\'s quiz score (0-100): '))
    assignment_score = int(input('Enter the student\'s assignment score (0-100): '))
    grades_weight = (test_score, quiz_score, assignment_score)
    students[students_name] = grades_weight
    print('Current student table is: ' + str(students))

def save_data(student_manager, course_manager):
    with open('students.json', 'w') as f:
        json.dump(student_manager.student_list, f)
    with open('courses.json', 'w') as f:
        json.dump(course_manager.course_list, f)
    print("Data saved successfully.")

def load_data(student_manager, course_manager):
    try:
        with open('students.json', 'r') as f:
            student_manager.student_list = json.load(f)
        with open('courses.json', 'r') as f:
            course_manager.course_list = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

# Initialize managers
student_manager = AddStudent()
course_manager = AddCourse()

# Load data if available
load_data(student_manager, course_manager)

# Main program loop
action = initialize()

while action != 9:
    if action == 1:
        student_manager.add_student()
    elif action == 2:
        course_manager.add_course()
    elif action == 3:
        course_manager.register_student_for_course(student_manager)
    elif action == 4:
        calculate_GPA_for_student(student_manager)
    elif action == 5:
        search_by_GPA(student_manager)
    elif action == 6:
        view_grade(student_manager)
    elif action == 7:
        save_data(student_manager, course_manager)
    elif action == 8:
        load_data(student_manager, course_manager)

    action = initialize()

print("Thank you for registering! Thanks for using the grade book!")

