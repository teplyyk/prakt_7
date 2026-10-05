INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    lines = f.readlines()

    line_count = len(lines)
    sum_grades_math = 0
    sum_grades_python = 0
    sum_grades_english = 0
    best_student = ['',0]

    for line in lines:
        line.strip()
        grades = line.split(",")
        for i in range(1, len(grades)):
            grades[i] = int(grades[i])
        if sum(grades[1:4]) >= best_student[1]:
            best_student[0] = grades[0]
            best_student[1] = sum(grades[1:4])
        sum_grades_math += grades[1]
        sum_grades_python += grades[2]
        sum_grades_english += grades[3]

    mid_grade_math = round(sum_grades_math / line_count,1)
    mid_grade_python = round(sum_grades_python / line_count,1)
    mid_grade_english = round(sum_grades_english / line_count,1)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write('Середній бал по класу:\n'
            f'math: {mid_grade_math}\n'
            f'python: {mid_grade_python}\n'
            f'english: {mid_grade_english}\n\n'
            f'Найкращий студент: {best_student}')

print('Середній бал по класу:\n'
      f'math: {mid_grade_math}\n'
      f'python: {mid_grade_python}\n'
      f'english: {mid_grade_english}\n\n'
      f'Найкращий студент: {best_student}')