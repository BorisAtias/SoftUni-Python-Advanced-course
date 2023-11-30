import os

def traverse_directory(dir_to_travers):
    file_info = {}

    """Минаваме през директорията и задаваме разширението като "key" в речника,
     а файловете ще апенднем в лист към него"""
    for file in os.listdir(dir_to_travers):
        if os.path.isfile(os.path.join(dir_to_travers, file)):
            filename, extension = os.path.splitext(file)
            if extension not in file_info:
                file_info[extension] = []
            file_info[extension].append(file)

    """Създаваме, или отваряме report.txt за писане и минаваме през ключовете с for loop,
    сортираме списъка с файлове към съответният ключ и записваме файл по файл, минаваики 
    през списъка с файлове с нов for цикъл"""
    with open(os.path.join(dir_to_travers, 'report.txt'), 'w') as report_file:
        for extension in file_info:
            files = sorted(file_info[extension])
            report_file.write(f"{extension}\n")
            for file in files:
                report_file.write(f"- {file}\n")
            report_file.write('\n') # Този ред не е според изискванията, но разделя групите разширения с празен ред
                                    #  и report.txt става малко по-четлив

dir_to_travers = ''  # <-- Въведете директорията/пътя тук!
traverse_directory(dir_to_travers)