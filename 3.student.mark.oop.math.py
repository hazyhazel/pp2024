import sys, os
from math import floor
import numpy as np
import curses

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

    @staticmethod
    def newStudent(stdscr):
        stdscr.clear()
        stdscr.addstr("Enter information for a new student:")
        
        name = getInput(stdscr, "\nEnter student's name: ")
        student_id = getInput(stdscr, "\nEnter student ID: ")
        dob = getInput(stdscr, "\nEnter student's date of birth: ")
        student = Student()
        student.setName(name) 
        student.setID(student_id)
        student.setDob(dob)
        
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

        
    def getName(self):
        return self._name 


    def getID(self):
        return self._id
    
    
    def getMarks(self):
        return self._marks
    
    
    def setMarks(self, stdscr):
        '''
        Assign marks for each student. Input attendance, midterm and final mark first,
        calculate GPA then append later to the list self._marks[student_id]
        '''
        stdscr.clear()
        student_id = getInput(stdscr, "Enter the student ID to input marks: ")
        
        if student_id in self._marks:
            stdscr.addstr(f"\nUpdating marks for student {student_id}")
        else:
            stdscr.addstr(f"\nAdding marks for student {student_id}") 
          
        attendance = int(getInput(stdscr, "\nEnter attendance mark: "))
        midterm = int(getInput(stdscr, "\nEnter midterm mark: "))
        final = int(getInput(stdscr, "\nEnter final mark: "))

        self._marks[student_id] = [attendance, midterm, final]

        gpa = self.calculateGPA(stdscr)
        if gpa != None:
            self._marks[student_id].append(gpa)
            stdscr.addstr(f"\nSuccessfully added/updated marks for student {student_id}\n")

        stdscr.refresh()
        stdscr.getch()
    
    
    def setWeights(self, stdscr):
        labels = ["attendance mark", "midterm mark", "final mark"]
        stdscr.clear()
        stdscr.addstr("Enter weights for each of the mark:")
        for i, label in enumerate(labels):
            stdscr.refresh()
            weight_str = getInput(stdscr, f"\nEnter weight for {label}: ")
            self.weights[i] = float(weight_str)
            
        stdscr.getch()
        stdscr.refresh()
    
    
    def calculateGPA(self, stdscr):
        stdscr.clear()
        student_id = getInput(stdscr, "Enter the student ID to calculate GPA: ")
        if student_id not in self._marks:
            stdscr.addstr(f"Student {student_id} has no marks assigned")
            return None
        
        # Take the first 3 marks only: attendance, midterm and final
        marks = np.array(self._marks[student_id][:3])
        
        gpa = np.sum(self.weights * marks)
        
        return gpa
        
        
    def showMarks(self, stdscr):
        '''
        Show marks of all students in the course
        '''
        stdscr.clear()
        if self._marks == {}:
            stdscr.addstr("No marks have been added to students in this course")
        else:
            stdscr.addstr("Displaying marks of students in this course: \n")
            for key, marks in self._marks.items():
                stdscr.addstr(
                    f"{key}:\n"
                    f"Attendance mark: {marks[0]}\n"
                    f"Midterm mark: {marks[1]}\n"
                    f"Final mark: {marks[2]}\n"
                    f"GPA: {marks[3]}"
                )
        stdscr.refresh()
        stdscr.getch()
        
        
    def sortbyGPA(self, stdscr):
        stdscr.clear()
        students_with_gpa = []
        for student_id, marks in self._marks.items():
            if marks[3] == None: # marks[3] is the GPA
                gpa = self.calculateGPA(stdscr)
            else:
                students_with_gpa.append((student_id, marks[3]))
        
        students_with_gpa.sort(key=lambda student : student[1], reverse=True) 
        # student[1] is the GPA each tuple
        
        stdscr.addstr("Students sorted by GPA in descending order:")
        for index, (student_id, gpa) in enumerate(students_with_gpa, start=1):
            stdscr.addstr(f"\n{index}. Student ID: {student_id}, GPA: {gpa}")  
        
        
    @staticmethod
    def newCourse(stdscr):
        stdscr.clear()
        stdscr.addstr("Enter information for a new course:")
        
        course_name = getInput(stdscr, "\nEnter course's name: ")
        course_id = getInput(stdscr, "\nEnter course's ID: ")
        
        course = Course()
        course.setName(course_name)
        course.setID(course_id)
        course.setWeights(stdscr)
        
        return course
            
            
class UI():
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.menu = [
            "1. Add a new student",
            "2. Add a new course",
            "3. Assign marks to a student in a course",
            "4. Show all students in a selected course",
            "5. Sort students by their GPA in descending order",
            "6. Exit"
        ]
        
        
    def start(self):
        self.stdscr.clear()
    
    
    def close(self):
        self.stdscr.addstr("\nPress any key to return to the menu.")
        self.stdscr.refresh()
        self.stdscr.getch()
        
    def displayMenu(self, index=0):
        """
        Display the menu
        """
        self.stdscr.clear()
        self.stdscr.addstr("Menu:\n", curses.A_BOLD)

        for idx, option in enumerate(self.menu):
            if idx == index:
                # Highlight the current option
                self.stdscr.addstr(f"{option}\n", curses.A_REVERSE)
            else:
                self.stdscr.addstr(f"{option}\n")

        self.stdscr.refresh()
    
        
    def run(self):
        highlight_idx = 0
        students = []
        courses = []
        
        while True:
            self.displayMenu(highlight_idx)

            key = self.stdscr.getch()

            if key == curses.KEY_UP and highlight_idx > 0:
                highlight_idx -= 1
            elif key == curses.KEY_DOWN and highlight_idx < len(self.menu) - 1:
                highlight_idx += 1
            elif key == ord('\n'):  # Enter to choose
                choice = highlight_idx + 1

                if choice == 1:
                    self.start()
                    student = Student.newStudent(self.stdscr)
                    students.append(student)
                    self.stdscr.addstr("\nNew student added! ")
                    self.close()
                    
                elif choice == 2:
                    self.start()
                    course = Course.newCourse(self.stdscr)
                    courses.append(course)
                    self.stdscr.addstr("\nNew course added! ")
                    self.close()
                    
                elif choice == 3:
                    self.start()
                    course = selectCourse(courses, self.stdscr)
                    if course:
                        course.setMarks(self.stdscr)
                        self.stdscr.addstr("\nMarks assigned! ")
                    self.close()
                    
                elif choice == 4:
                    self.start()
                    course = selectCourse(courses, self.stdscr)
                    if course:
                        course.showMarks(self.stdscr)
                    self.close()
                    
                elif choice == 5:
                    self.start()
                    course = selectCourse(courses, self.stdscr)
                    if course:
                        course.sortbyGPA(self.stdscr)
                    self.close()

                elif choice == 6:
                    self.start()
                    self.stdscr.addstr("Exiting...")
                    self.close()
                    break
    
            
def selectCourse(course_list, stdscr):
    '''
    Select a course from the course list to later display students' info and marks
    '''
    if course_list == []:
        stdscr.addstr("This course list is empty.")
        stdscr.refresh()
        stdscr.getch()
        return None
    
    stdscr.clear()
    stdscr.addstr("\nSelect a course by entering its ID: ")
    for idx, course in enumerate(course_list, start=1):
        stdscr.addstr(f"\n{idx}. ID: {course._id} - Course: {course._name}")
    stdscr.refresh()
    
    choice = getInput(stdscr, "\nEnter course ID: ")
    
    selected = next((course for course in course_list if course._id == choice), None)
    if not selected:
        stdscr.addstr("\nThis course does not exist.\n")
        stdscr.refresh()
        stdscr.getch()
        
    return selected


def getInput(stdscr, prompt):
        """
        Allows the user to type input from keyboard and display spontaneously on the screen
        """
        stdscr.addstr(prompt)

        input_str = ""
        while True:
            key = stdscr.getch()

            if key in [curses.KEY_ENTER, 10, 13]: # (ASCII 10 ='\n', 13 = '\r')
                break
            elif key in [curses.KEY_BACKSPACE, 8, 127]:  
                if len(input_str) > 0:
                    input_str = input_str[:-1]
                    y, x = stdscr.getyx()  
                    if x > 0:
                        stdscr.move(y, x - 1)  
                        stdscr.delch()         
            elif key >= 32 and key <= 126: # ASCII range
                input_str += chr(key) # convert ASCII to characters
                stdscr.addstr(chr(key))

            stdscr.refresh()

        return input_str.strip()  


def main(stdscr):
    curses.curs_set(0)
    ui = UI(stdscr)
    ui.run()
    
if __name__ == "__main__":
    curses.wrapper(main)