# Input the number of students in a class
def number_of_student():
    num_students = int(input("Number of students in class: "))

    if num_students > 0:
        return num_students
    else:
        print("The number of students must be positive. Enter the number of students in class again: ")


# Input student information: id, name, DoB
def student_info():
    student_id = input("Student ID: ")
    student_name = input("Student's name: ")
    student_dob = input("Student's date of birth: ")

    return student_id, student_name, student_dob


# Input the number of courses
def number_of_courses():
    num_courses = int(input("Number of courses: "))
    
    if num_courses < 0:
        return num_courses
    else:
        print("The number of courses must be positive. Enter the number of courses again: ")


# Input course information: id, name
def course_info():
    course_id = input("Course ID: ")
    course_name = input("Course's name: ")

    return course_id, course_name


# Input marks for student in a selected course
def input_mark(course_name):
    midterm_mark = float(input("Enter midterm mark for " + course_name + " : "))
    final_mark = float(input("Enter final mark for " + course_name + " : "))

    return midterm_mark, final_mark


