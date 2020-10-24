with open('english.txt', 'r', encoding='utf-8') as english:
    with open('russian.txt', 'a', encoding='utf-8') as russian:
        for line in english:
            word = line.split()
            russian.write(line.replace(word[0], input(f"Enter translation for {word[0]}: ")))
