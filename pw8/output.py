from domains import Student, Course
from input import *
from to_file import *
import curses
import threading

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
        self.students_file = "students.txt"
        self.courses_file = "courses.txt"
        
        
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


    def loadData(self, filename):
        try:
            return decompressAndUnpickle(filename)
        except IOError:
            print(f"Failed to load this file")
            # Return students and courses as empty lists
            return [], []


    def saveData(self, students, courses, filename):
        pickleAndCompress(students, courses, filename)

        
    def run(self):
        students, courses = self.loadData("students.dat")
        highlight_idx = 0
    
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
                
        students, courses = self.loadData("students.dat")

    # Background Daemon thread does not stop the main thread from exiting
        background_thread = threading.Thread(
            target=self.saveData, args=(10, "students.dat", students, courses), daemon=True)
        background_thread.start()