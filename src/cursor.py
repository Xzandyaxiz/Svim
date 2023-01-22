import os

class Cursor:
    def __init__(self, text) -> None:
        self.text = text
        self.cursor = (0, 0)

        self.rows = self.text.split('\n')

    def update_cursor(self, message = None):
        os.system('clear')

        text_index = self.get_cursor_position()
        char_arr = [char for char in self.text]

        if text_index >= len(char_arr)-1:
            return

        if char_arr[text_index] == '\n':
            char_arr.insert(text_index, "\u258e")

        char_arr[text_index] = "\033[47m" + char_arr[text_index] + "\033[0m"
        rows = ''.join(char_arr).split('\n')

        for row in rows:
            print(f'\033[36m~\033[0m  {row}')

        print(message) if message else 0

    def move_cursor_row(self, amount):
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

        self.cursor = (self.cursor[0] + amount, self.cursor[1])
        return self.update_cursor()

    def move_cursor_col(self, amount):
        if self.cursor[1] + amount < 0:
            return

        if self.cursor[1] + amount > len(self.rows[self.cursor[0]]):
            self.cursor = (self.cursor[0] + amount, 0)
        
            return self.update_cursor()

        self.cursor = (self.cursor[0], self.cursor[1] + amount)
        return self.update_cursor()


    def get_cursor_position(self):
        text_index = 0

        for row in range(self.cursor[0]):
            text_index += len(self.rows[row]) + 1

        text_index += self.cursor[1]

        return text_index