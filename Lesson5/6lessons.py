from re import findall

subj = {}
with open('lessons.txt', 'r', encoding='utf-8') as lessons:
    for lesson in lessons:
        subj[lesson[0:len(lesson.split(":")[0])]] = sum([int(num) for num in findall(r"\d+", lesson)])
    print(f'Hours for each lesson - {subj}')
