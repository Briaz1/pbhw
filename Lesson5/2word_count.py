lines_count = 0
with open('words_count.txt', 'r', encoding='utf-8') as words:
    for num, line in enumerate(words, 1):
        print(f'In {num} line {len(line.split())} words.')
        lines_count += 1
    print(f'In {words.name} file {lines_count} lines!')
