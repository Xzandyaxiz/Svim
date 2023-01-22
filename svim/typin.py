""" Handles everything related to typing and other key actions """

from .cursor import Cursor

class Typing:
    def __init__(self, cursor: Cursor):
        self.cursor = cursor

    def add_letter(self, letter):
        text_index = self.cursor.get_cursor_position()
        self.cursor.text = self.cursor.text[:text_index] + letter + self.cursor.text[text_index:]
        self.cursor.rows = self.cursor.text.split('\n')

        self.cursor.cursor = (self.cursor.cursor[0], self.cursor.cursor[1] + 1)

        self.cursor.update_cursor()

    def delete_forward(self):
        text_index = self.cursor.get_cursor_position()

        if not self.cursor.cursor[1] < len(self.cursor.rows[self.cursor.cursor[0]]):
            return
        
        self.cursor.text = self.cursor.text[:text_index] + self.cursor.text[text_index+1:]
        self.cursor.rows = self.cursor.text.split('\n')
        
        self.cursor.update_cursor()

    def backspace(self):
        text_index = self.cursor.get_cursor_position()
        
        self.cursor.text = self.cursor.text[:text_index-1] + self.cursor.text[text_index:]
        self.cursor.rows = self.cursor.text.split('\n')
        
        if self.cursor.cursor[1] == 0:
            self.cursor.cursor = (self.cursor.cursor[0]-1, len(self.cursor.rows[self.cursor.cursor[0]-1]))
        
        else:
            self.cursor.cursor = (self.cursor.cursor[0], self.cursor.cursor[1]-1)
        
        self.cursor.update_cursor()