from input import *
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