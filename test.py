import shutil

while True:

    columns, rows = shutil.get_terminal_size()
    print("Number of rows:", rows)
    print("Number of columns:", columns)