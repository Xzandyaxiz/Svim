""" Handles everything related to cursor actions or cursor movements """

class Cursor:
    def __init__(self, text) -> None:
        self.text = text
        self.cursor = (0, 0)

        self.rows = self.text.split('\n')
        self.row_des = 0
        self.shift_held = False
        self.selection_start = None
        self.selection_end = None
        self.undo_array = []

    def parse_previous_move(self):
        cursor, text = self.undo_array[-1].split(';')

        return (cursor, text)

    def undo(self):
        pass

    def update_cursor(self, message = None, undo_string = None):
        print('\033c', end='', flush=True)

        if undo_string:
            self.undo_array.append(undo_string)

        text_index = self.get_cursor_position()
        char_arr = [char for char in self.text]

        if text_index >= len(char_arr)-1:
            return

        if char_arr[text_index] == '\n':
            char_arr.insert(text_index, "\u258e")

        char_arr[text_index] = "\033[47m" + char_arr[text_index] + "\033[0m"
        rows = ''.join(char_arr).split('\n')

        for row in rows:
            print(f'\r\033[36m~\033[0m  {row}')

        print(self.cursor)
        print(message) if message else 0

    def move_cursor_row(self, amount, undo_string):
        if self.cursor[0] + amount < 0:
            return
            
        try:
            if self.cursor[1] > len(self.rows[self.cursor[0] + amount]):
                self.cursor = (self.cursor[0] + amount, 0)
                return self.update_cursor()

            elif not self.rows[self.cursor[0]+amount].strip():
                self.cursor = (self.cursor[0] + amount, 0)
                return self.update_cursor()

        except IndexError:
            return
        
        if len(self.rows[self.cursor[0] + amount]) >= self.row_des:
            self.cursor = (self.cursor[0], self.row_des)
        
        else:
            self.cursor = (self.cursor[0], len(self.rows[self.cursor[0] + amount]) )

        self.cursor = (self.cursor[0] + amount, self.cursor[1])

        return self.update_cursor(undo_string=f"{str(self.cursor)};{self.text}")

    def move_cursor_col(self, amount, undo_string):
        if self.cursor[1] + amount < 0:
            return

        if self.cursor[1] + amount > len(self.rows[self.cursor[0]]):
            self.cursor = (self.cursor[0] + amount, 0)
        
            return self.update_cursor()
        
        if len(self.rows[self.cursor[0]]) >= self.row_des:
            self.row_des += amount

        self.cursor = (self.cursor[0], self.cursor[1] + amount)

        return self.update_cursor(undo_string=f"{str(self.cursor)};{self.text}")


    def get_cursor_position(self):
        text_index = 0

        for row in range(self.cursor[0]):
            text_index += len(self.rows[row]) + 1

        text_index += self.cursor[1]

        return text_index

    