# Input the number of students in a class
def number_of_student():
    num_students = int(input("Number of students in class: "))

    if num_students > 0:
        return num_students
    else:
        print("The number of students must be positive. Enter the number of students in class again: ")


# Input student information: id, name, DoB
def student_information(num_students):
    '''
    Create a dictionary to store the info of students with keys are IDs 
    and values are dictionaries that store name, dob and marks
    '''
    students = {}
    for i in range(num_students):
        print(f"\nStudent {i+1}")
        student_id = input("Student ID: ")
        student_name = input("Student's name: ")
        student_dob = input("Student's date of birth: ")
        students[student_id] = { 
            "name": student_name, 
            "dob": student_dob, 
            "marks": {}
            }

    return students


# Input the number of courses
def number_of_courses():
    num_courses = int(input("\nNumber of courses: "))
    
    if num_courses > 0:
        return num_courses
    else:
        print("The number of courses must be positive. Enter the number of courses again: ")


# Input course information: id, name
def course_information(num_courses):
    '''
    Create a list to store info of courses, including a dictionary "students"
    '''
    courses = []
    for i in range(num_courses):
        course_id = input("\nCourse ID: ")
        course_name = input("Course's name: ")
        courses.append({
            "id": course_id, 
            "name": course_name, 
            "students": {}
            }
        )

    return courses


# List all courses with their corresponding index
def list_courses(courses):
    for index, course in enumerate(courses, 1):
        print(f"\nCourse {index}:")
        print(f"ID: {course['id']} - Name: {course['name']}")


# List out all students
def list_students(students):
    print("\nList of all students")
    for index, (student_id, student_info) in enumerate(students.items(), 1):
        print(f"{index}. ID: {student_id} - Name: {student_info['name']}\n")


# Select a course
def select_course(courses):
    choice = input("\nSelect a course by entering its ID: ")
    # Search for the a course that contains the matching ID in the list "courses", print None if not found
    selected = next((course for course in courses if course["id"] == choice), None)

    return selected


# Input marks for student in a selected course
def input_marks(courses, students):
    '''
    Select a course and enter marks for midterm and final exams for each student
    '''
    selected = select_course(courses)

    print(f"Input marks for {selected['name']} course")
    for student_id, student_info in students.items():
        print(f"Entering marks for student {student_info['name']}: ")
        midterm_mark = float(input("Enter midterm mark for " + selected["name"] + ": "))
        final_mark = float(input("Enter final mark for " + selected["name"] + ": "))
        selected["students"][student_id] = {
            "name": student_info["name"],
            "marks": {
                "midterm": midterm_mark,
                "final": final_mark
            }
        }


# Show student marks for a given course
def show_marks(courses):
    selected = select_course(courses)
    for student_id, student_info in selected["students"].items():
        marks = student_info["marks"]
        print(f"\nName: {student_info['name']}")
        print(f"ID: {student_id}")
        print(f"Midterm mark: {marks['midterm']}")
        print(f"Final mark: {marks['final']}")


# Input num of students
num_students = number_of_student()
# Enter students' info
students = student_information(num_students)
# Input num of course
num_courses = number_of_courses()
# Enter courses' info
courses = course_information(num_courses)
# List all courses
list_courses(courses)
# List all students
list_students(students)

# Input mảrks for a course
input_marks(courses, students)
# Show marks of a course
show_marks(courses)
