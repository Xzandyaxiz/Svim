import os

def update_cursor(cursor: tuple, rows: list, text: str) -> None:
    os.system('clear')
    text_index = 0

    try:
        for i in range(cursor[0]):
            text_index += len(rows[i]) + 1

        text_index += cursor[1]

        char_arr = [char for char in text]
        char_arr[text_index] = "\033[47m" + char_arr[text_index] + "\033[0m"

        print(''.join(char_arr))
        print(cursor)
    except:
        pass

def move_cursor_row(amount, cursor: tuple, rows: list):
    global cursor

    if cursor[0] + amount < 0:
        return
    try:

        if amount == -1:
            if cursor[1] > len(rows[cursor[0] - 1]):
                cursor = (cursor[0] + (amount +1), len(rows[cursor[0] - 1]) -1)

        if amount == 1:
            if cursor[1] > len(rows[cursor[0] + 1]):
                cursor = (cursor[0] + (amount - 1), len(rows[cursor[0] + 1]) -1)
    except IndexError:
        return

    cursor = (cursor[0] + amount, cursor[1])
    update_cursor(cursor, rows)


def move_cursor_col(amount: int, cursor: tuple):
    global cursor

    if cursor[1] + amount < 0:
        return
        
    cursor = (cursor[0], cursor[1] + amount)
    update_cursor()