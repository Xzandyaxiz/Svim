import sys
import termios
import tty
import os

cursor = (0, 0)

with open (sys.argv[1], 'r') as fp:
    text = fp.read()

rows = text[:].split('\n')

def update_cursor(message:str = None):
    os.system('clear')

    text_index = get_cursor_position()
    char_arr = [char for char in text]

    if text_index >= len(char_arr)-1:
        return

    if char_arr[text_index] == '\n':
        char_arr.insert(text_index, "\u258e")

    char_arr[text_index] = "\033[47m" + char_arr[text_index] + "\033[0m"
    rows = ''.join(char_arr).split('\n')

    for row in rows:
        print(f'\033[36m~\033[0m  {row}')
        
    print(message) if message else 0

def move_cursor_row(amount):
    global cursor

    if cursor[0] + amount < 0:
        return
        
    try:

        if cursor[1] > len(rows[cursor[0] + amount]):
            cursor = (cursor[0] + amount, 0)
            return update_cursor()

        elif not rows[cursor[0]+amount].strip():
            cursor = (cursor[0] + amount, 0)
            return update_cursor()

    except IndexError:
        return

    cursor = (cursor[0] + amount, cursor[1])
    return update_cursor()

def move_cursor_col(amount):
    global cursor
    global rows

    if cursor[1] + amount < 0:
        return

    if cursor[1] + amount > len(rows[cursor[0]]):
        cursor = (cursor[0] + amount, 0)
    
        return update_cursor()

    cursor = (cursor[0], cursor[1] + amount)
    update_cursor()

def add_letter(letter):
    global cursor
    global text
    
    text_index = get_cursor_position()

    text = text[:text_index] + letter + text[text_index:]
    rows = text.split('\n')

    cursor = (cursor[0], cursor[1] + 1)
    
    update_cursor()

def get_cursor_position():
    global cursor
    global text
    global rows

    text_index = 0
    for i in range(cursor[0]):
        text_index += len(rows[i]) + 1

    text_index += cursor[1]

    return text_index

def delete_forward():
    global text
    global cursor
    global rows

    text_index = get_cursor_position()

    if not cursor[1] < len(rows[cursor[0]]):
        return
    
    text = text[:text_index] + text[text_index+1:]
    rows = text.split('\n')
    
    update_cursor()

def backspace():
    global text
    global cursor

    text_index = get_cursor_position()

    text = text[:text_index-1] + text[text_index:]
    rows = text.split('\n')

    if cursor[1] == 0:
        cursor = (cursor[0]-1, len(rows[cursor[0]-1]))

    else:
        cursor = (cursor[0], cursor[1]-1)

    update_cursor()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def run():
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

            update_cursor(f"\n(Saved {sys.argv[1]})")

        elif key == '\x1b':
            key = getch()
            if key == '[':
                key = getch()
                if key == 'A':
                    move_cursor_row(-1)
                elif key == 'B':
                    move_cursor_row(1)
                elif key == 'C':
                    move_cursor_col(1)
                elif key == 'D':
                    move_cursor_col(-1)

        elif key == '\x7f':
            backspace()
        
        elif key == chr(127):
            delete_forward()

        else:
            add_letter(key)

if __name__ == '__main__':
    os.system('clear')
    update_cursor()
    run()