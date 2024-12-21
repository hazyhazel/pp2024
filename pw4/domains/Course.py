from input import *
from math import floor
import numpy as np
import curses

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