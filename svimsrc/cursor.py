from .config import CONFIG
import sys, shutil

class Cursor:
    def __init__(self, text = None):
        self.text = text
        self.row_des = 0
        self.cursor = (0, 0)

        self.config = CONFIG('config.json').get_highlighting(sys.argv[1])

    def refresh(self):
        rows = self.text.split('\n')
        visual_rows = []

        rows_num = shutil.get_terminal_size()[1]

        if len(rows) > rows_num:
            #if self.cursor[0] > len(rows) - 5:
            #    pass
            
            for row in range(rows_num - 3):
                visual_rows.append(rows[row])

        else:
            visual_rows = rows        

        current_row = visual_rows[self.cursor[0]]
        current_char = ''

        if len(current_row) > self.cursor[1]:
            current_char = current_row[self.cursor[1]]
        
        else:
            current_char = ' '

        cursor_char = f'\033[30;47m{current_char}\033[39;49m'
        visual_rows[self.cursor[0]] = current_row[:self.cursor[1]] + cursor_char + current_row[self.cursor[1]+1:] 

        updated_screen = []

        for row in visual_rows:
            updated_screen.append(f'\033[36m~\033[39m {row} ')

        screen = '\033c' + f'\033[30;47m' + ' ' * 30 + f'FILE: {sys.argv[1]}' + ' ' * 40 + '\033[39;49m\n' + '\n'.join(updated_screen) + f'\n{self.cursor}\n'

        print('\033[?25l')

        print(screen, end='\r', flush=True)

    def move_cursor_row(self, amount):
        rows = self.text.split('\n')

        if self.cursor[0] + amount >= len(rows):
            return

        elif self.cursor[0] + amount < 0:
            self.row_des = 0
            return

        elif self.cursor[1]+1 > len(rows[self.cursor[0] + amount]):
            self.cursor = (self.cursor[0] + amount, len(rows[self.cursor[0] + amount]))

        else:
            self.cursor = (self.cursor[0] + amount, self.cursor[1])

        if len(rows[self.cursor[0]]) > self.row_des:
            self.cursor = (self.cursor[0], self.row_des)

        elif len(rows[self.cursor[0]]) <= self.row_des:
            self.cursor = (self.cursor[0], len(rows[self.cursor[0]]))

            if self.cursor[1] > 0:
                self.row_des = self.cursor[1]

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

        self.row_des += amount

        return self.refresh()