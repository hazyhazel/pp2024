import curses

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