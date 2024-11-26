# Input the number of students in a class
def number_of_student():
    num_students = int(input("Number of students in class: "))

    if num_students > 0:
        return num_students
    else:
        print("The number of students must be positive. Enter the number of students in class again: ")


# Input student information: id, name, DoB
def student_info():
    students = []
    num_students = number_of_student()
    for i in range(num_students):
        print(f"\nStudent {i+1}")
        student_id = input("Student ID: ")
        student_name = input("Student's name: ")
        student_dob = input("Student's date of birth: ")
        student_marks = []
        students.append({"id": student_id, "name": student_name, "dob": student_dob, "marks": {}})

    return students


# Input the number of courses
def number_of_courses():
    num_courses = int(input("Number of courses: "))
    
    if num_courses > 0:
        return num_courses
    else:
        print("The number of courses must be positive. Enter the number of courses again: ")


# Input course information: id, name
def course_info():
    courses = []
    num_courses = number_of_courses()
    for i in range(num_courses):
        course_id = input("Course ID: ")
        course_name = input("Course's name: ")
        courses.append({"id": course_id, "name": course_name, "students": {}})

    return courses


# List all courses with their corresponding index
def list_courses(courses):
    for index, course in enumerate(courses, 1):
        print(f"Course {index}:\n")
        print(f"ID: {course["id"]} - Name: {course["name"]}")


# Input marks for student in a selected course
def input_mark(courses):
    '''
    Select a course and enter marks for midterm and final exams for each student
    '''
    
    choice = input("Select a course by entering its ID: ")
    # Search for the a course that contains the matching ID in the list "courses", print None if not found
    selected = next((course for course in courses if course["id"] == choice), None)

    print(f"Input marks for {selected["id"]} {selected["name"]} course")
    for student_name in selected["students"].items():
        print(f"\nEntering marks for student {student_name}: ")
        midterm_mark = float(input("Enter midterm mark for " + selected["name"] + " : "))
        final_mark = float(input("\nEnter final mark for " + selected["name"] + " : "))
        student_info["marks"] = {"midterm": midterm_mark, "final": final_mark}

    return # this is a void function

