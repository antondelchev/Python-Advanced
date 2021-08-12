words = list(input())
reversed_words = []

while words:
    reversed_words.append(words.pop())

print("".join(reversed_words))
