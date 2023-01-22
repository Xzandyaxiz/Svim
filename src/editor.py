import sys, termios, tty, os
from cursor import Cursor
from typin import Typing

with open (sys.argv[1], 'r') as fp:
    text = fp.read()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def run(cursor: Cursor):
    typing = Typing(cursor)

    while True:

        key = getch()

        if key == 'q':
            os.system('clear')
            break

        elif key == chr(24):
            os.system('clear')

            with open (sys.argv[1], 'w') as fp:
                fp.write(text)
            
            break

        elif key == chr(19):
            with open (sys.argv[1], 'w') as fp:
                fp.write(text)

            cursor.update_cursor(f"\n(Saved {sys.argv[1]})")

        elif key == '\x1b':
            key = getch()
            if key == '[':
                key = getch()
                if key == 'A':
                    cursor.move_cursor_row(-1)
                elif key == 'B':
                    cursor.move_cursor_row(1)
                elif key == 'C':
                    cursor.move_cursor_col(1)
                elif key == 'D':
                    cursor.move_cursor_col(-1)

        elif key == '\x7f':
            typing.backspace()
        
        elif key == chr(127):
            typing.delete_forward()

        else:
            typing.add_letter(key)

if __name__ == '__main__':
    os.system('clear')
    cursor = Cursor(text)
    cursor.update_cursor()

    run(cursor)