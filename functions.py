PATH = "todos.txt"


def get_todos(filepath=PATH):   # custom function to get 'todos' file with argument as filepath
    with open(filepath, 'r') as file:  # with context manager
        todos_local = file.readlines()  # variable scope - local
    return todos_local  # if there's no return, implicitly it prints out None


def write_todos(todos_arg, filepath=PATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)