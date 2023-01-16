def add_letter(letter: str, text: str, cursor: tuple, rows: list) -> None:
    global cursor
    global text
    global rows

    text_index = 0
    for i in range(cursor[0]):
        text_index += len(rows[i]) + 1

    text_index += cursor[1]

    text = text[:text_index] + letter + text[text_index:]
    rows = text.split('\n')
    cursor = (cursor[0], cursor[1] + 1)

    update_cursor()

def backspace(text: str, rows: list, cursor: tuple) -> None:
    global cursor
    global text
    global rows
    text_index = 0
    for i in range(cursor[0]):
        text_index += len(rows[i]) + 1
    text_index += cursor[1]
    text = text[:text_index-1] + text[text_index:]
    rows = text.split('\n')
    if cursor[1] == 0:
        cursor = (cursor[0]-1, len(rows[cursor[0]-1]))
    else:
        cursor = (cursor[0], cursor[1]-1)
    update_cursor()