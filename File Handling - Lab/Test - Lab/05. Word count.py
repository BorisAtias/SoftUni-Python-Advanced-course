import re
from collections import Counter
"""
# Read the list of words from words.txt
with open('words.txt', 'r') as words_file:
    words_list = words_file.read().split()

# Read the text from text.txt
with open('text.txt', 'r') as text_file:
    text = text_file.read()

# Perform case-insensitive word frequency counting using regular expressions
word_count = Counter(re.findall(r'\w+', text, re.IGNORECASE))

# Sort the word count dictionary by frequency in descending order
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

# Write the results to another text file
with open('results.txt', 'w') as results_file:
    for word, frequency in sorted_word_count.items():
        results_file.write(f'{word}: {frequency}\n')
"""

with open("words.txt", "r") as f:
    searched_words = f.read().lower().split()

with open("text.txt", "r") as f:
    text = f.read().lower()

words = {}

for searched_word in searched_words:

    pattern = re.compile(rf"\b{searched_word}\b")
    result = re.findall(pattern, text)
    words[searched_word] = len(result)

with open('output_1.txt', 'w') as results_file:
    for key, value in sorted(words.items(), key=lambda item: -item[1]):
        results_file.write(f'{key}: {value}\n')
