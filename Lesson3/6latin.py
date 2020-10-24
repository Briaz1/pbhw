def int_func(words):
    for i in words:
        if 97 <= ord(i) <= 122 or ord(i) == 32:
            pass
        else:
            words = words.replace(i, "", 1)
    words = words.split()
    for num, word in enumerate(words):
        words[num] = word.capitalize()
    words = " ".join(words)

    return words


print("This program accepts only small Latin letters. The rest of the characters will be mercilessly removed!")
print(int_func(input("Enter words in small latin letters: ")))
