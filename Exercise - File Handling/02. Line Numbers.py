import string

with open("text.txt", "r") as input_f:
    with open("output.txt", "w") as output_f:
        for number, line in enumerate(input_f.readlines(), start=1):
            alpha = len([x for x in line if x.isalpha()])
            punctuation = len([char for char in line if char not in string.whitespace and not char.isalnum()])
            output_f.write(f'Line {number}: {line} ({alpha})({punctuation})\n')

"""
Импортваме модула string, който за съжаление не се поддържа в Judge! Отваряме text.txt за четене и 
output.txt за писане! Правим for loop за да минем през редовете! Правим comprehension за да преброим
буквите(и използваме len(), за броят им веднага) и пишем съответният резултат в output.txt!
"""