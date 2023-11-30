symbols_to_replace = ["-", ",", ".", "!", "?"]

with open("text.txt", "r") as f:
    for index, line in enumerate(f, start=0):
        if index % 2 == 0:
            words = line.split()
            reverse_words = words[::-1]
            final_line = ""

            for word in reverse_words:
                final_word = ""
                for symbol in word:
                    if symbol in symbols_to_replace:
                        final_word += "@"
                    else:
                        final_word += symbol

                final_line += final_word + " "

            print(final_line.strip())

"""
Задаваме списък със символите, които трябва да заменим. Отваряме работният файл за четене!
Правим for loop и използваме enumerate стартирайки от 0 за да хванем и първият(нулев) ред!
Правим проверка за четните редове и отделяме думите със .split()! Обръщаме реда на думите
и създаваме празен стринг за финалният принт!
Правим for loop за да минем през думите и още един, за да минем през буквите във всяка дума! Правим си празен
стринг, който да преме обработената дума. Правим необходимите проверки и след всяка дума добавяме думата към 
създаденият по-рано стринг final_print и добавяме интервал за да раделя думите. Обираме със Strip() излишният интервал накрая 
"""