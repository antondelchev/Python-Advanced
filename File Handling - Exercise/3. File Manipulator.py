import os.path

command = input()

while not command == "End":
    command = command.split("-")
    order, file_name = command[0], command[1]

    if order == "Create":
        file = open(file_name, "w")
        file.close()
    elif order == "Add":
        content = command[2]
        with open(file_name, "a") as file:
            file.write(content)
            file.write("\n")
    elif order == "Replace":
        old_string = command[2]
        new_string = command[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as file:
                content = file.read().replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(content)
        else:
            print("An error occurred")
    elif order == "Delete":
        if os.path.exists(file_name):
            pass
            os.remove(file_name)
        else:
            print("An error occurred")

    command = input()
