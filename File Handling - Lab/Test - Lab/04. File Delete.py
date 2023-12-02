# SoftUni lection

import os
my_working_dir = os.path.dirname(os.path.abspath(__file__))  # Those two rows are optional! If the file is in the same dir we dont need those
file_path = os.path.join(my_working_dir, "output_1.txt")

try:
    os.remove(file_path)
except FileNotFoundError:
    print("File already deleted!")

# Under is a program made to search the entire PC to find the file we want deleted

"""import os


def delete_file_by_name(file_name):
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully.")
            return

    print(f"File '{file_name}' not found.")


# Example usage
file_name = "xxHomeworkxx.py"  # Replace with the file name you want to delete
delete_file_by_name(file_name)"""

# And here is a version to delete all occurrences if more files with the same name should be deleted


"""import os


def delete_all_files_by_name(file_name):
    deleted = False
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            file_paths = [os.path.join(root, file) for file in files if file == file_name]
            for file_path in file_paths:
                os.remove(file_path)
            deleted = True

    if deleted:
        print(f"All files with the name '{file_name}' deleted successfully.")
    else:
        print(f"No files with the name '{file_name}' found.")


# Example usage
file_name = "example.txt"  # Replace with the file name you want to delete
delete_all_files_by_name(file_name)"""