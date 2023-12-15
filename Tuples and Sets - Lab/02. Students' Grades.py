student_count = int(input())

students = {}

for _ in range(student_count):

    name, score = input().split()

    if not name in students:
        students[name] = [float(score)]
    else:
        students[name].append(float(score))


for name, scores in students.items():
    formatted_scores = ' '.join(f'{score:.2f}' for score in scores)
    avg_score = sum(scores) / len(scores)
    print(f"{name} -> {formatted_scores} (avg: {avg_score:.2f})")