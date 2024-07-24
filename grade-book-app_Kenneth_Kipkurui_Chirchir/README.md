Grade Book Utility
This Python-based Grade Book Utility allows users to manage student records, courses, and grades interactively. It includes features for adding students, courses, registering students for courses, viewing grades, and saving/loading data.

Features
Add Student: Add a new student to the grade book with their name and email.
Add Course: Add a new course with details such as course name, trimester, and credits.
Register Student for Course: Register an existing student for a course.
View Grade: Update and view a student's test, quiz, and assignment scores.
Save Data: Save student and course data to JSON files.
Load Data: Load student and course data from JSON files.
Classes
AddStudent
Attributes: student_list - List to store student records.
Methods:
add_student(): Prompts user to enter student details and adds the student to student_list.
AddCourse
Attributes: course_list - List to store course records.
Methods:
add_course(): Prompts user to enter course details and adds the course to course_list.
register_student_for_course(student_manager): Registers a student for a course by adding the course to the student's record.
