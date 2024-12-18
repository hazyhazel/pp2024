from math import floor
import numpy as np

class Student:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._dob = ""
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


    def newStudent():
        print("Enter information for a new student:")
        student = Student()
        
        student.setName(input("Enter student's name: \n")) 
        student.setID(input("Enter student ID: "))
        student.setDob(input("Enter student's date of birth: "))
        
        return student
        
        
class Course:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._marks = {} # {student: [attendance, midterm mark, final mark]}
        self.weights = np.zeros(3, dtype=float)
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


    def setMarks(self):
        '''
        Assign marks for each student. Input attendance, midterm and final mark first,
        calculate GPA then append later to the list self._marks[student_id]
        '''
        student_id = input("Enter the student ID to input marks: ")
        if student_id in self._marks:
            print(f"Updating marks for student {student_id}")
        else:
            print(f"Adding marks for student {student_id}") 
            attendance = floor(float(input("Enter attendance mark: ")))
            midterm = floor(float(input("Enter midterm mark: ")))
            final = floor(float(input("Enter final mark: ")))
            self._marks[student_id] = [attendance, midterm, final]
            
            gpa = self.calculateGPA()
            if gpa != None:
                self._marks[student_id].append(gpa)
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
                    f"Attendance mark: {marks[0]}\n"
                    f"Midterm mark: {marks[1]}\n"
                    f"Final mark: {marks[2]}\n"
                    f"GPA: {marks[3]}"
                )
    
    
    def setWeights(self):
        labels = ["attendance mark", "midterm mark", "final mark"]
        print("Enter weights for each of the mark:")
        for i, label in enumerate(labels):
            self.weights[i] = float(input(f"Enter weight for {label}: "))
    
    
    def calculateGPA(self):
        student_id = input("Enter the student ID to calculate GPA: ")
        if student_id not in self._marks:
            print(f"Student {student_id} has no marks assigned")
            return None
        
        # Take the first 3 marks only: attendance, midterm and final
        marks = np.array(self._marks[student_id][:3])
        
        gpa = np.sum(self.weights * marks)
        
        return gpa
        
        
    def newCourse():
        print("Enter information for a new course:")
        
        course = Course()
        course.setName(input("Enter course's name: "))
        course.setID(input("Enter course's ID: "))
        course.setWeights()
        
        return course
            
            
def selectCourse(course_list):
    '''
    Select a course from the course list to later display students' info and marks
    '''
    if course_list == []:
        print("This course list is empty.")
    else:
        choice = input("\nSelect a course by entering its ID: ")
        selected = next((course for course in course_list if course._id == choice), None)
        
        return selected

def main():
    students = []
    courses = []

    while True:
        print("\n--- Options ---")
        print("1. Add a new student")
        print("2. Add a new course")
        print("3. Assign marks to a student in a course")
        print("4. Show all students in a selected course")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            student = Student.newStudent()
            students.append(student)
            print("New student added!")

        elif choice == "2":
            course = Course.newCourse()
            courses.append(course)
            print("New course added!")

        elif choice == "3":
            course = selectCourse(courses)
            if course:
                course.setMarks()
                print("Marks assigned!")

        elif choice == "4":
            course = selectCourse(courses)
            if course:
                course.showMarks()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()