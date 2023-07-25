from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%F:%S")
print("Today is ", now)

while True:
    user_action = input("Type Add, Show, Edit, Commplete or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo.capitalize() + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new ToDo: ") + "\n"
            todos[number] = new_todo

            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:].strip())

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)

            message = f"ToDo {todo_to_remove} has been removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Invalid Input!")

print("Bye")
