from domains import *
from input import *
from output import *

def main(stdscr):
    curses.curs_set(0)
    ui = UI(stdscr)
    ui.run()
    
if __name__ == "__main__":
    curses.wrapper(main)