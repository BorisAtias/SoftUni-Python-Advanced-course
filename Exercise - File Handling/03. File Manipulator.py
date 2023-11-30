import os

"""
Функцията приема име на файл и го създава, в случай,
че не съществува файл с това име
"""
def create_file(file_name):
    with open(file_name, "w") as file:
        pass

"""
Функция приемаща име на файл и съдържание! Съдържанието се попълва във файла
"""
def add_new_content(file_name, content):
    with open(file_name, "a") as file:
        file.write(f"{content}\n")

"""
Функцията приема име на файл, елементи, които следва да бъдат заменени ин елемент, с които заменяме вече съществуващият!
Първо отваряме и четем съдържанието. После с .replace() подменяме елементите зачислявайки промененият текст към променлива
После отваряме файла за писане и пренаписваме съдържанието подавайки променливата.
В случай, че не съществува файл с това име, печатаме грешка!
"""
def replace_content(file_name, old_string, new_string):
    try:
        with open(file_name, "r") as file:
            content = file.read()

        updated_content = content.replace(old_string, new_string)

        with open(file_name, "w") as file:
            file.write(updated_content)
    except FileNotFoundError:
        print("An error occurred")

"""
Функцията приема име на файл и ако сушествува, го изтрива! Иначе печата грешка!
"""
def file_delete(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


while True:

    command = input().split("-")

    if command[0] == "End":
        break
    file_name = command[1]

    if command[0] == "Create":
        create_file(file_name)
    elif command[0] == "Add":
        content = command[2]
        add_new_content(file_name, content)
    elif command[0] == "Replace":
        old_string, new_string = command[2], command[3]
        replace_content(file_name, old_string, new_string)
    elif command[0] == "Delete":
        file_delete(file_name)

"""
Във безкрайният луп приемаме комадите СПЛИТНАТИ("-") за сда разделим съдържанието!
След това, според зависи от командата, извикваме съответната функция и подаваме съответните елементи!
"""