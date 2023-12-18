text = input()

unique_chars = set()

for char in text:
    unique_chars.add(char)

char_counts = []

for char in unique_chars:
    count = text.count(char)
    char_counts.append((char, count))

char_counts.sort()

for char, count in char_counts:
    print(f"{char}: {count} time/s")
