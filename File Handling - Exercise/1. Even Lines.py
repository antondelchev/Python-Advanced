file = open("text_1.txt", "r")

counter = 0
for line in file:
    for el in line:
        if el in ".,-!?":
            line = line.replace(el, "@")
    if counter % 2 == 0:
        reversed_text = line.split()[::-1]
        print(" ".join(reversed_text))
    counter += 1

file.close()
