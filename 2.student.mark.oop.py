class Student:
    def __init__(self):
        self._ID = ""
        self._name = ""
        self._dob = ""
        self.marks = {}
        
        def __str__(self):
            return f"{self._ID} - {self._name} - {self._dob}"
    
        def setName(self, name):
            if isinstance(name, str) and name != "":
                self._name = name
            else:
                print("Invalid input of name. Enter name again: ")
        
        def setID(self, id):
            if isinstance(id, str) and id != "":
                self._ID = id
            else:
                print("Invalid input of ID. Enter again: ")
        
        def setDob(self, dob):
            if isinstance(dob, str) and dob != "":
                self._dob = dob
            else:
                print("Invalid input of date of birth. Enter again: ")
        
        def setMarks(self, marks):
            pass
        
        def getName(self):
            return self._name
        
        def getID(self):
            return self._ID
        
        def getDob(self):
            return self._dob
        
        def newStudent():
            print("Enter information for a new student: \n")
            student = Student()
            
            student.setName(input("Enter student's name: \n")) 
            student.setID(input("Enter student ID: "))
            student.setDob(input("Enter student's date of birth: \n"))
            
            return student
        
        
class Course:
    def __init__(self):
        self._ID = ""
        self._name = ""
        self._marks = {}
        
        def __str__(self):
            return f"Course: {self._ID} - {self._name}"
        
        def setName(self, name):
            if isinstance(name, str) and name != "":
                self._name = name
            else:
                print("Invalid input of name. Enter name again: ")
        
        def setID(self, id):
            if isinstance(id, str) and id != "":
                self._ID = id
            else:
                print("Invalid input of ID. Enter again: ")

        def setStudents(self, student : str):
            if student in self._marks.keys():
                print("Updating mark for this student: ")
            else:
                print("Adding mark for this student: ")
                
            self._marks[student] = [
                float(input("Enter midterm mark: ")),
                float(input("Enter final mark: "))
            ]
            
        def newCourse():
            print("Enter information for a new course: \n")
            
            course = Course()
            course.setName(input("Enter course's name: \n"))
            course.setID(input("Enter course's ID: \n"))
            course.setStudents(input("Enter student's name to enter marks: \n"))
            
            

            
            
            