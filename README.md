# Svim
Svim (Super vim) is a terminal based text editor similar to vim.

Currently only supports systems based on gnu/linux.

import sys, termios, tty
from svimsrc import Cursor
from svimsrc import Typing

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
            flush()
            break

        elif key == '\x1b':
            handle_arrow_keys(key, cursor)
        
        elif key == '\x7f':
            typing.backspace()

        elif key == '\n':
            typing.newline()

        elif key == chr(19):
            with open (sys.argv[1], 'w+') as fp:
                fp.write(cursor.text)

            print(f"(Wrote to '{sys.argv[1]}')")

        else:
            typing.add_letter(key)

def flush():
    print('\033c', end='\r', flush=True)

def handle_arrow_keys(key, cursor):

    key = getch()
    if key != '[':
        return

    key = getch()
    if key == 'A':
        cursor.move_cursor_row(-1)
    elif key == 'B':
        cursor.move_cursor_row(1)
    elif key == 'C':
        cursor.move_cursor_col(1)
    elif key == 'D':
        cursor.move_cursor_col(-1)

if __name__ == "__main__":
    cursor = Cursor(text)
    cursor.refresh()

    run(cursor)