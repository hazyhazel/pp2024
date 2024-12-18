class Student:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._dob = ""
        self._marks = {}
        self._students = []
        
    def __str__(self):
        '''
        List all students' information
        '''
        for student in self._students:
            return f"{self._id} - {self._name} - {self._dob}"

    def setName(self, name):
        if isinstance(name, str) and name != "":
            self._name = name
        else:
            print("Invalid input of name. Enter name again: ")
    
    def setID(self, id):
        if isinstance(id, str) and id != "":
            self._id = id
        else:
            print("Invalid input of ID. Enter again: ")
    
    def setDob(self, dob):
        if isinstance(dob, str) and dob != "":
            self._dob = dob
        else:
            print("Invalid input of date of birth. Enter again: ")
    
    def getName(self):
        return self._name
    
    def getID(self):
        return self._id
    
    def getDob(self):
        return self._dob

    def newStudent(self):
        print("Enter information for a new student: \n")
        student = Student()
        
        student.setName(input("Enter student's name: \n")) 
        student.setID(input("Enter student ID: "))
        student.setDob(input("Enter student's date of birth: \n"))
        self._students.append(student)
        
        return student
        
        
class Course:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._marks = {} # {student: [midterm, final]}
        self._courses = []
        
    def __str__(self):
        '''
        List all courses' information
        '''
        for course in self._courses:
            return f"Course: {self._id} - {self._name}"
    
    def setName(self, name):
        if isinstance(name, str) and name != "":
            self._name = name
        else:
            print("Invalid input of name. Enter name again: ")
    
    def setID(self, id):
        if isinstance(id, str) and id != "":
            self._id = id
        else:
            print("Invalid input of ID. Enter again: ")

    def setMarks(self, student_id : str):
        student_id = input("Enter the student ID to input marks: ")
        if student_id in self._marks:
            print("Updating the marks for this student")
        else:
            print("Adding marks for this student")
            midterm = float(input("Enter midterm mark: "))
            final = float(input("Enter final mark: "))
            self._marks[student_id] = [midterm, final]
            print(f"Successfully added/updated for student {student_id}")
        
    def getName(self):
        return self._name 

    def getID(self):
        return self._id
    
    def getMarks(self):
        return self._marks
    
    def showMarks(self):
        '''
        Show marks of all students in the course
        '''
        if self._marks == {}:
            print("No marks have been added to students in this course")
        else:
            print("Displaying marks of students in this course: ")
            for key, marks in self._marks.items():
                print(
                    f"{key}:\n"
                    f"Midterm mark: {marks[0]}\n"
                    f"Final mark: {marks[1]}"
                )
        
    def newCourse(self):
        print("Enter information for a new course: \n")
        
        course = Course()
        course.setName(input("Enter course's name: \n"))
        course.setID(input("Enter course's ID: \n"))
        course.setStudents(input("Enter student's name to enter marks: \n"))
        self._courses.append(course)
        
        return course
            
            
def selectCourse(course_list, choice):
    '''
    Select a course from the course list to later display students' info and marks
    '''
    if course_list == []:
        print("This course list is empty.")
    else:
        choice = input("\nSelect a course by entering its ID: ")
        selected = next((course for course in course_list if course._id == choice), None)
        
        return selected