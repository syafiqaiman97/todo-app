# Class : Day_015
# (Standard Modules & Git )
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip the space from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]  # list slicing: it will read the character at index 4 and so on [4:0]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        # Method 1: For-Loops
        """
        new_todos = []

        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        """
        # Method 2: List-Comprehensions
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')  # Method 3: Direct changes
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is invalid")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("That is beyond the current list")
            continue
        except ValueError:
            print("Your command is invalid")
            continue
    elif user_action.startswith("exit"):
        break

    else:
        print("Command is invalid!")

print("Bye!")
