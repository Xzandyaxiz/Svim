class Cursor:
    def __init__(self, text = None):
        self.text = text
        self.cursor = (0, 0)

    def refresh(self):
        print('\033c', end='', flush=True)
        rows = self.text.split('\n')

        current_row = rows[self.cursor[0]]
        current_char = ''

        if len(current_row) > self.cursor[1]:
            current_char = current_row[self.cursor[1]]
        
        else:
            current_char = ' '

        cursor_char = f'\033[30;47m{current_char}\033[39;49m'
        rows[self.cursor[0]] = current_row[:self.cursor[1]] + cursor_char + current_row[self.cursor[1]+1:] 

        for row in rows:
            print(f'\033[36m~\033[39m {row} ')

        print(self.cursor)

    def move_cursor_row(self, amount):
        rows = self.text.split('\n')

        if self.cursor[0] + amount >= len(rows):
            return

        elif self.cursor[0] + amount < 0:
            return

        elif self.cursor[1]+1 > len(rows[self.cursor[0] + amount]):
            self.cursor = (self.cursor[0] + amount, len(rows[self.cursor[0] + amount]))

        else:
            self.cursor = (self.cursor[0] + amount, self.cursor[1])

        return self.refresh()

    def move_cursor_col(self, amount):
        rows = self.text.split('\n')

        if self.cursor[1] + amount > len(rows[self.cursor[0]]):
            if self.cursor[0] + 1 >= len(rows):
                return
                
            self.cursor = (self.cursor[0] + 1, 0)

        elif self.cursor[1] + amount < 0:
            return self.move_cursor_row(-1)

        else:
            self.cursor = (self.cursor[0], self.cursor[1] + amount)

        return self.refresh()