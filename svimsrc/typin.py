from .cursor import Cursor

class Typing:
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    def add_letter(self, char):
        rows = self.cursor.text.split('\n')
        current_row = rows[self.cursor.cursor[0]]

        rows[self.cursor.cursor[0]] = current_row[:self.cursor.cursor[1]] + char + current_row[self.cursor.cursor[1]:]
        self.cursor.text = '\n'.join(rows)

        self.cursor.move_cursor_col(1)

        return self.cursor.refresh()

    def backspace(self):
        rows = self.cursor.text.split('\n')
        current_row = rows[self.cursor.cursor[0]]

        if self.cursor.cursor[1] - 1 < 0:
            return
            
        rows[self.cursor.cursor[0]] = current_row[:self.cursor.cursor[1]-1] + current_row[self.cursor.cursor[1]:]
        self.cursor.text = '\n'.join(rows)

        self.cursor.move_cursor_col(-1)

    def newline(self):
        self.add_letter('\n')