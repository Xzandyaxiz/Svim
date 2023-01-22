""" Alternative to Vim with an easy to use default configuration similar to that of the nano editor """

from svim import Cursor
from svim import Typing
from svim import Input

import sys

text = ""

if len(sys.argv) > 0:
    with open (sys.argv[1], 'r') as fp:
        text = fp.read()

def run(cursor: Cursor):
    typing = Typing(cursor)

    while True:
        key = Input().getch()

        if key == 'q':
            handle_q()
            break

        elif key == chr(24):
            handle_ctrl_x()
            break
        elif key == chr(19):
            handle_ctrl_s(cursor)
        elif key == '\x1b':
            handle_arrow_keys(key, cursor)
        elif key == '\x7f':
            typing.backspace()
        elif key == chr(127):
            typing.delete_forward()
        else:
            typing.add_letter(key)

def handle_q():
    flush()

def handle_ctrl_x():
    flush()
    with open (sys.argv[1], 'w') as fp:
        fp.write(text)

def handle_ctrl_s(cursor):
    with open (sys.argv[1], 'w') as fp:
        fp.write(text)
    cursor.update_cursor(f"\n(Saved {sys.argv[1]})")

def handle_arrow_keys(key, cursor):
    key = Input().getch()
    if key != '[':
        return
    key = Input().getch()

    if key == 'A':
        cursor.move_cursor_row(-1)
    elif key == 'B':
        cursor.move_cursor_row(1)
    elif key == 'C':
        cursor.move_cursor_col(1)
    elif key == 'D':
        cursor.move_cursor_col(-1)

def flush():
    print('\033c', end='', flush=True)

if __name__ == '__main__':
    flush()

    cursor = Cursor(text)
    cursor.update_cursor()

    run(cursor)