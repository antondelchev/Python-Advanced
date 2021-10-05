file = open("text_2.txt", "r")

counter = 1
for line in file:
    line = line.strip()
    punctuation_marks = 0
    spaces = 0
    for el in line:
        if not el.isalpha() and not el == " ":
            punctuation_marks += 1
        if el == " ":
            spaces += 1
    print(f"Line {counter}: {line} ({len(line) - punctuation_marks - spaces})({punctuation_marks})")
    counter += 1

file.close()
